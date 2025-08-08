// card order 
document.addEventListener('DOMContentLoaded', function () {

  let checking = document.querySelector('.checking')
  let names = document.querySelectorAll('.name-of-product')
  let prices = document.querySelectorAll('.price')

  // get data from local storage
  let arrayProduct = JSON.parse(localStorage.getItem('arrayProduct')) || [];

  arrayProduct.forEach(element => {
    let productName = element.productName
    let productPrice = element.prices
    let productPid = element.pid
    let vendorVid = element.vid
    let qun = element.qun


    
  
    
    let html =`
    <div style="display: flex; width: 100%; justify-content: space-around;"> 
      <div class="text-muted"  style="text-align: center;">
      <h6>name: </h6>
        <p style="display:none;" >${vendorVid}</p>
        <p style="display:none;" > ${productPid}</p>
        
          <span class="font-weight-bold text-dark">
          <p>${productName}</p>
        </span>
      </div>
      
      <div class="text-muted" style="text-align: center;">
        <h6>Color: </h6>
        <span class="font-weight-bold text-dark">
        <p></p>
      </span>
      </div>

      <div class="text-muted" style="text-align: center;">
        <h6>quantity </h6>
        <span class="font-weight-bold text-dark">
          <p>${qun}</p>
        </span>
      </div>

      <div class="text-muted" style="text-align: center;">
        <h6>price: </h6>
        <span class="font-weight-bold text-dark">
          <p>${productPrice}</p>
        </span>
      </div>

      <input class="inputeProductName" type="hidden" name="productName[]" value="${productName}" />
      <input class="inputPrice" type="hidden" name="price[]" value="${productPrice}" />
      <input class="input-product-id" type="hidden"  name="product_id[]" value="${productPid}" />
      <input class="input-vendor-id" type="hidden"  name="vendor_id[]" value="${vendorVid}" />
      <input class="qun" type="hidden"  name="qun[]" value="${qun}" />

    </div>
    <hr style="height:20px" />
    `
    //  document.querySelectorAll('.vendor-id') = vendorVid
    //  document.querySelectorAll('.product-id')  = productPid
    checking.innerHTML += html

    

  
    

    // function ordernow() {
    //   // let productElement = this.closest(".checking");
    //   // let productId = productElement.dataset.productId;
    //   // console.log(productId);

    //   let nameInputs = document.querySelectorAll('.inputeProductName')
    //   let priceInputs = document.querySelectorAll('.inputPrice')
    //   let inputProductId = document.querySelectorAll('.input-product-id')
    //   let inputvendorId = document.querySelectorAll('.input-vendor-id')
    
    //   for (let i = 0; i < productName.length; i++) {
    //     nameInputs[i].value = productName[i].innerText;
    //     priceInputs[i].value = productPrice[i].innerText;
    //     inputProductId[i].value = productPid[i].innerText;
    //     inputvendorId[i].value = productPid[i].innerText;
        
        
    //   }}
  });

  



})