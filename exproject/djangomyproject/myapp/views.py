from django.shortcuts import render

# ฟังก์ชันแสดงรายการสินค้า
def product_list(request):
    return render(request, 'product_list.html')

# ฟังก์ชันแสดงรายละเอียดสินค้า
def product_detail(request, product_id):
    return render(request, 'product_detail.html')

def product_html1(request):
    return render(request, 'product1.html')

def product_html2(request):
    return render(request, 'product2.html')

def product_html3(request):
    return render(request, 'product3.html')