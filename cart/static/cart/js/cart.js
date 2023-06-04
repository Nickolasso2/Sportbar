// show and hide editQuantityForm while press edit
function editQuantity(event){
  for (let element of event.currentTarget.parentElement.getElementsByClassName('quantityEdit')){
    element.setAttribute('style', 'display:inline-block; ')
  }
  for (let element of event.currentTarget.parentElement.getElementsByClassName('quantityReal')){
    element.style.display = 'none'
  }
}

// show and hide editQuantityForm while press confirm/close
function confirmClose(event){
  event.preventDefault(event);
  // show and hide editQuantityForm
  for (let element of event.currentTarget.parentElement.getElementsByClassName('quantityEdit')){
    element.setAttribute('style', 'display:none;')
  }
  for (let element of event.currentTarget.parentElement.getElementsByClassName('quantityReal')){
  element.style.display = 'inline-block'
  }
}


// =======================confirmation/submit of editing quantity

// adding events for every editQuantityForms
let editQuantityForms = document.getElementsByClassName('editQuantityForm');
for (let  editQuantityForm of  editQuantityForms) {
    editQuantityForm.addEventListener('submit', function(event){
        event.preventDefault(event);
        // show and hide editQuantityForm
        confirmClose(event)
        sendRequestFetchPost('POST', this.action, new FormData(this))
    })
}

function sendRequestFetchPost(method, url, body) {
  return fetch(url, {
      method : method,
      body : body,
      headers: {
        "X-Requested-With": "XMLHttpRequest",
      },
  }).then((response) => response.json())
.then((data) => showCartEdited(data.product_id, data.newTotalProductPrice, data.newTotal, data.newQuantity))
.catch((error) => console.log(error))
}

// put fetch response into html
function showCartEdited(product_id, newTotalProductPrice, newTotal, newQuantity){
  document.getElementById(`${product_id}_total_price`).innerText = newTotalProductPrice;
  document.getElementById('cart_total_cost').innerText = newTotal;
  document.getElementById(`${product_id}_quantity`).innerText = newQuantity;
}


// =========================check if cart not empty for display empty/not empty cart
fetch(document.getElementById('is_cart_url').value)
.then(response => response.json())
.then((response) => {
  if(response.response == 'yes'){
    emptyCart.style.display = 'none';
    goodsNumber.innerText = response.goodsNumber;} else {
      notEmptyCart.style.display = 'none';
}
})
// =========================/check if cart not empty for display empty/not empty cart