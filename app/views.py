from django.shortcuts import render
from app.models import Wheel, Nav, Mustbuy, Shop, MainShow, Foodtypes, Goods


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
def market(request, categoryid):
    # 分类数据
    foodtypes = Foodtypes.objects.all()

    # 获取点击 历史 [typeIndex]
    # 有typeIndex
    # 无typeIndex，默认0
    typeIndex = int(request.COOKIES.get('typeIndex',0))
    print(foodtypes[typeIndex])
    categoryid = foodtypes[typeIndex].typeid


    # 商品数据
    # goodslist = Goods.objects.all()[1:10]
    # 根据商品分类 数据过滤
    goodslist = Goods.objects.filter(categoryid=categoryid)

    data = {
        'title': '闪购超市',
        'foodtypes':foodtypes,
        'goodslist':goodslist
    }

    return render(request, 'market.html', context=data)

# 购物车
def cart(request):
    return render(request, 'cart.html')

# 我的
def mine(request):
    return render(request, 'mine.html')