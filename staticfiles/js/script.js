(function($) {
  
  
  "use strict";

  var initPreloader = function() {
    $(document).ready(function($) {
    var Body = $('body');
        Body.addClass('preloader-site');
    });
    $(window).load(function() {
        $('.preloader-wrapper').fadeOut();
        $('body').removeClass('preloader-site');
    });
  }

  // init Chocolat light box
	var initChocolat = function() {
		Chocolat(document.querySelectorAll('.image-link'), {
		  imageSize: 'contain',
		  loop: true,
		})
	}

  var initSwiper = function() {
    
    // swiper slider home 2
    $('.slideshow').each(function(){
      var space = $(this).attr('data-space') ? $(this).attr('data-space') : 0 ;
      var col = $(this).attr('data-col');
      if ( typeof col == "undefined" || !col) {
        col = 1;
      }

      var swiper = new Swiper(".slideshow", {
        slidesPerView: col,
        spaceBetween: space,
        speed: 1000,
        loop: true,
        navigation: {
          nextEl: '.icon-arrow-right',
          prevEl: '.icon-arrow-left',
        },
        pagination: {
          el: ".slideshow-swiper-pagination",
          clickable: true,
        },
      });
    });

    var category_swiper = new Swiper(".category-carousel", {
      slidesPerView: 8,
      spaceBetween: 30,
      speed: 500,
      navigation: {
        nextEl: ".category-carousel-next",
        prevEl: ".category-carousel-prev",
      },
      breakpoints: {
        0: {
          slidesPerView: 2,
        },
        768: {
          slidesPerView: 3,
        },
        991: {
          slidesPerView: 5,
        },
        1500: {
          slidesPerView: 8,
        },
      }
    });

    var brand_swiper = new Swiper(".brand-carousel", {
      slidesPerView: 4,
      spaceBetween: 30,
      speed: 500,
      navigation: {
        nextEl: ".brand-carousel-next",
        prevEl: ".brand-carousel-prev",
      },
      breakpoints: {
        0: {
          slidesPerView: 2,
        },
        768: {
          slidesPerView: 2,
        },
        991: {
          slidesPerView: 3,
        },
        1500: {
          slidesPerView: 4,
        },
      }
    });

    var products_swiper = new Swiper(".products-carousel", {
      slidesPerView: 5,
      spaceBetween: 30,
      speed: 500,
      navigation: {
        nextEl: ".products-carousel-next",
        prevEl: ".products-carousel-prev",
      },
      breakpoints: {
        0: {
          slidesPerView: 1,
        },
        768: {
          slidesPerView: 3,
        },
        991: {
          slidesPerView: 4,
        },
        1500: {
          slidesPerView: 5,
        },
      }
    });

    // product single page
    var thumb_slider = new Swiper(".product-thumbnail-slider", {
      slidesPerView: 5,
      spaceBetween: 20,
      // autoplay: true,
      direction: "vertical",
      breakpoints: {
        0: {
          direction: "horizontal"
        },
        992: {
          direction: "vertical"
        },
      },
    });

    var large_slider = new Swiper(".product-large-slider", {
      slidesPerView: 1,
      // autoplay: true,
      spaceBetween: 0,
      effect: 'fade',
      thumbs: {
        swiper: thumb_slider,
      },
      pagination: {
        el: ".swiper-pagination",
        clickable: true,
      },
    });
  }

  // Animate Texts
  var initTextFx = function () {
    $('.txt-fx').each(function () {
      var newstr = '';
      var count = 0;
      var delay = 100;
      var stagger = 10;
      var words = this.textContent.split(/\s/);
      var arrWords = new Array();
      
      $.each( words, function( key, value ) {
        newstr = '<span class="word">';

        for ( var i = 0, l = value.length; i < l; i++ ) {
          newstr += "<span class='letter' style='transition-delay:"+ ( delay + stagger * count ) +"ms;'>"+ value[ i ] +"</span>";
          count++;
        }
        newstr += '</span>';

        arrWords.push(newstr);
        count++;
      });

      this.innerHTML = arrWords.join("<span class='letter' style='transition-delay:"+ delay +"ms;'>&nbsp;</span>");
    });
  }

  // input spinner
  var initProductQty = function(){

    $('.product-qty').each(function(){
      var $el_product = $(this);
      var quantity = 0;
      $el_product.find('.quantity-right-plus').click(function(e){
        e.preventDefault();
        var quantity = parseInt($el_product.find('.quantity').val());
        $el_product.find('.quantity').val(quantity + 1);
      });

      $el_product.find('.quantity-left-minus').click(function(e){
          e.preventDefault();
          var quantity = parseInt($el_product.find('.quantity').val());
          if(quantity>0){
            $el_product.find('.quantity').val(quantity - 1);
          }
      });

    });

  }

  // init jarallax parallax
  var initJarallax = function() {
    jarallax(document.querySelectorAll(".jarallax"));

    jarallax(document.querySelectorAll(".jarallax-keep-img"), {
      keepImg: true,
    });
  }

  // document ready
  $(document).ready(function() {
    
    initPreloader();
    initTextFx();
    initSwiper();
    initProductQty();
    initJarallax();
    initChocolat();

  }); // End of a document

})(jQuery);

// normel JS


document.addEventListener('DOMContentLoaded', function () {
  // تعريف البائع الحالي
  let currentVendorId = document.querySelector('.vendor-id')?.textContent.trim();

  // جلب السلة من التخزين
  let arrayProduct = JSON.parse(localStorage.getItem('arrayProduct')) || [];

  // ✅ تحقق إذا كانت السلة تخص بائعًا آخر
  if (arrayProduct.length > 0 && arrayProduct[0].vId !== currentVendorId) {
    localStorage.removeItem('arrayProduct');
    arrayProduct = [];
    location.reload(); // لإفراغ الصفحة من منتجات البائع الآخر
    return;
  }

  // تعريف العناصر
  let nameOfProduct = document.querySelectorAll('.name-of-product');
  let productPid = document.querySelectorAll('.product-pid');
  let vendorId = document.querySelectorAll('.vendor-id');
  let categoryOfProduct = document.querySelectorAll('.category-of-product');
  let priceInProItem = document.querySelectorAll('.price-in-pro-item');
  let quantityOneProduct = document.querySelectorAll('.quantity-one-product');
  let btnAddCard = document.querySelectorAll('.btn-add-card');
  let listGroup = document.querySelector('.list-group');

  // رسم المنتجات من التخزين
  arrayProduct.forEach((storedProduct) => {
    let i = Array.from(productPid).findIndex(el => el.textContent.trim() === storedProduct.pid);
    if (i !== -1) createItem(i);
  });

  for (let i = 0; i < btnAddCard.length; i++) {
    btnAddCard[i].addEventListener('click', function () {
      let productName = nameOfProduct[i].textContent.trim();
      let pid = productPid[i].textContent.trim();
      let vId = vendorId[i].textContent.trim();
      let qun = quantityOneProduct[i].value;

      if (!arrayProduct.some(item => item.pid === pid)) {
        let prices = parseFloat(priceInProItem[i].textContent.trim()) * parseInt(quantityOneProduct[i].value);
        arrayProduct.push({ productName, prices, pid, vId, qun });
        createItem(i);
        localStorage.setItem("arrayProduct", JSON.stringify(arrayProduct));
      } else {
        console.log("product already in cart");
      }
    });
  }

  function createItem(i) {
    let productName = nameOfProduct[i].textContent.trim();
    let unitPrice = parseFloat(priceInProItem[i].innerHTML);
    let quantity = parseInt(quantityOneProduct[i].value) || 1;
    let totalPriceOne = unitPrice * quantity;

    let li = document.createElement('li');
    li.className = 'list-group-item d-flex justify-content-between lh-sm list-group-item-card';
    li.innerHTML = `
      <div>
        <h6 class="my-0 name-of-product">${productName}</h6>
        <small class="text-body-secondary category-of-product">${categoryOfProduct[i].innerText.trim()}</small>
      </div>
      <h4 class="text-body-secondary price-in-pro-item price-for-one" style="margin-top: 6px;">${totalPriceOne}</h4>
      <p style="margin-top:8px;">x${quantity}</p>
      <button class="btn btn-danger delete-item-pro" type="button">
        <i class="bi bi-trash"></i> Delete
      </button>

    `;

    listGroup.appendChild(li);
    updateTotalPrice();
    updateCount();

    li.querySelector('.delete-item-pro').addEventListener('click', function () {
      listGroup.removeChild(li);
      let index = arrayProduct.findIndex(item => item.productName === productName);
      if (index !== -1) arrayProduct.splice(index, 1);
      localStorage.setItem("arrayProduct", JSON.stringify(arrayProduct));
      updateTotalPrice();
      updateCount();
    });
  }

  function updateTotalPrice() {
    let total = 0;
    document.querySelectorAll('.price-for-one').forEach(item => {
      total += parseFloat(item.innerHTML);
    });
    document.querySelector('.totals-price').innerHTML = total + ' DA';
  }

  function updateCount() {
    let count = arrayProduct.length;
    document.querySelector('.badge').innerHTML = count;
    document.querySelector('.count-for-card-icon').innerHTML = count;
  }









});
