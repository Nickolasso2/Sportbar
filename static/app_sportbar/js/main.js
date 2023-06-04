// ===================Slider=======================

let slideIndex = 0;
    showSlides();
    
    function showSlides() {
      let slides = document.getElementsByClassName("mySlides");
      // mySlides are on home page only  
      if (slides[0]){
        let i;
        let dots = document.getElementsByClassName("dot");
        for (i = 0; i < slides.length; i++) {
          slides[i].style.display = "none";  
        }
        slideIndex++;
        if (slideIndex > slides.length) {slideIndex = 1}    
        for (i = 0; i < dots.length; i++) {
          dots[i].className = dots[i].className.replace(" active", "");
        }
        slides[slideIndex-1].style.display = "block";  
        dots[slideIndex-1].className += " active";
        setTimeout(showSlides, 7000); // Change image every 7 seconds

      }
    }

//  ===================///Slider=======================


// =======================modal window adding to cart
function passInModal(event){
  // it's from data-get-product-title
let getProductTitle = event.currentTarget.dataset.getProductTitle
let elementWithIdAttribute = document.getElementById(getProductTitle)

// get product id from data-get-product-title
let productId = getProductTitle.slice(10);
let form = document.getElementById(`addToCartForm${productId}`);

if(form.querySelector('input[type=number]').value == 0){
  document.getElementById('exampleModalLabel').innerText = 'Too fast...';
  document.getElementById('cartMessage').innerText = 'Looks like you forgot to enter the quantity you need...'
  document.getElementById('addToCartButton2').setAttribute('style', 'display:none;')
  } else{
    document.getElementById('exampleModalLabel').innerText = 'Greate choice!';
    document.getElementById('cartMessage').innerText = `You are going to add ${elementWithIdAttribute.innerText} to your shopping cart`
    document.getElementById('addToCartButton2').setAttribute('style', 'display:inline-block;')

    // submiting form
    document.getElementById('addToCartButton2').addEventListener('click', function(){
    form.submit()
    })
}}

// =======================///modal window adding to cart

// ====================Modal success confirmation window
function addSuccessModal(elementForm, modalTitleText,modalBodyText){
  
  elementForm.addEventListener('submit', function fetchSubmit(event){
    event.preventDefault(event);
    fetch(this.action, {
      method : 'POST',
      body : new FormData(this),
      
  }).then((response) => response.json())
      .then((response) => {
        console.log(response.response)
        if(response.response=='success') {
          document.getElementsByClassName('confirmationSuccess')[0].setAttribute('style', 'display:block;');
          modalTitle.innerText = modalTitleText;
          modalBody.innerText = modalBodyText;
      } else {document.getElementById(`${elementForm.id}Error`).innerText = 'Validation error'}
      })
  })

}

if (document.getElementById('bookTableForm')) {addSuccessModal(document.getElementById('bookTableForm'), 'Congtrats,  you\'ve booked a table', 'We\'re waiting for you');}

if (document.getElementById('OrderForm')) {
  addSuccessModal(document.getElementById('OrderForm'), 'Your order was successfull completed!', 'We\'ll do our best to deliver it to you ASAP.');
}


addSuccessModal(document.getElementById('SubscribeForm'), 'You\'he just successfully subscribed for our newsletter!', 'From now you are aware.');

function goHome(event){
  document.getElementsByClassName('confirmationSuccess')[0].setAttribute('style', 'display:none;');
  window.location.href = event.currentTarget.dataset['goHome']
}
// ====================///Modal success confirmation window


