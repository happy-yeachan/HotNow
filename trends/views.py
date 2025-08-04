from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, generics, status
from .models import TrendKeyword
from .serializers import TrendKeywordSerializer
from math import radians, cos, sin, asin, sqrt

class TrendListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        category = request.data.get('category')  # optional
        radius = 3000  # 반경 3키로 고정

        # 위치 정보 추출 (1순위: 요청 바디, 2순위: 유저 DB)
        user_lat, user_lng = self.get_location(request)
        if user_lat is None or user_lng is None:
            return Response([], status=status.HTTP_200_OK)

        # 카테고리 여부에 따라 queryset 선택
        if category:
            queryset = TrendKeyword.objects.filter(category=category)
        else:
            queryset = TrendKeyword.objects.all()

        # 거리 필터링 + score 정렬
        filtered = self.filter_by_distance(queryset, user_lat, user_lng, radius)
        serializer = TrendKeywordSerializer(filtered, many=True)
        return Response(serializer.data)

    def get_location(self, request):
        # 요청에 location이 포함되어 있다면 → 우선 사용
        location_param = request.data.get('location')
        if location_param:
            try:
                lat_str, lng_str = location_param.split(',')
                return float(lat_str), float(lng_str)
            except:
                return None, None

        # 없으면 → 로그인한 유저의 기본 위치
        user = request.user
        if user.location_lat and user.location_lng:
            return float(user.location_lat), float(user.location_lng)

        return None, None

    def filter_by_distance(self, queryset, user_lat, user_lng, radius):
        # 두 좌표 간 거리(m)를 계산하는 함수 (Haversine 공식)
        def haversine(lat1, lon1, lat2, lon2):
            R = 6371000  # 지구 반지름 (m)
            d_lat = radians(lat2 - lat1)
            d_lon = radians(lon2 - lon1)
            a = sin(d_lat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(d_lon / 2) ** 2
            c = 2 * asin(sqrt(a))
            return R * c  # 최종 거리 (미터)

        nearby = []

        # 각 트렌드 키워드의 위치와 사용자 위치 비교
        for item in queryset:
            if item.latitude and item.longitude:
                distance = haversine(
                    user_lat, user_lng,
                    float(item.latitude), float(item.longitude)
                )

                # 반경 내에 있으면 리스트에 추가
                if distance <= radius:
                    nearby.append(item)

        return sorted(nearby, key=lambda x: x.score, reverse=True)[:10]


class TrendDetailView(generics.RetrieveAPIView):
    queryset = TrendKeyword.objects.all()
    lookup_field = 'pk'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        # 트렌드 키워드 기본 정보
        base_data = TrendKeywordSerializer(instance).data

        # trend_event_log 기반 mock 데이터 (여기선 하드코딩 or 임시 생성)
        base_data['trend_graph'] = [
            {"time": "2025-08-02T12:00:00", "mention_count": 10},
            {"time": "2025-08-02T13:00:00", "mention_count": 24}
        ]

        # 연관 키워드 (임시)
        base_data['related_keywords'] = ["홍대데이트", "홍대카페"]

        # 연관 콘텐츠 (예: 인스타, 블로그 등)
        base_data['related_contents'] = [
            {
                "source": "instagram",
                "title": "홍대 핫한 맛집 리뷰",
                "url": "https://insta.com/post/123"
            }
        ]

        return Response(base_data)