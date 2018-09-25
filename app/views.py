from django.shortcuts import render
from app.models import Wheel, Nav, Mustbuy, Shop, MainShow


# 首页
def home(request):
    # 轮播图数据
    wheels = Wheel.objects.all()

    # 导航 数据
    navs = Nav.objects.all()

    # 每日必购
    mustbuys = Mustbuy.objects.all()

    # 商品部分
    shoplist = Shop.objects.all()
    shophead = shoplist[0]
    shoptab = shoplist[1:3]
    shopclass = shoplist[3:7]
    shopcommend = shoplist[7:11]

    # 商品主体
    mainshows = MainShow.objects.all()

    data = {
        'title': '首页',
        'wheels':wheels,
        'navs':navs,
        'mustbuys':mustbuys,
        'shophead':shophead,
        'shoptab':shoptab,
        'shopclass':shopclass,
        'shopcommend':shopcommend,
        'mainshows': mainshows
    }

    return render(request, 'home.html', context=data)

# 闪购超市
def market(request):
    return render(request, 'market.html')

# 购物车
def cart(request):
    return render(request, 'cart.html')

# 我的
def mine(request):
    return render(request, 'mine.html')