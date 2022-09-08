//'use strict';
var payment_url = document.location.href
console.log('payment url: ', payment_url)


function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

var paymentForm = document.getElementById("payment-form");
var orderConfirmation = document.getElementById("orderConfirmation");
var eftAlert = document.getElementById("eft-alert");
var breadCrumb = document.getElementById("breadcrumb");
var shopInformation = document.getElementById("shop-information");

$("#payment-form").submit(function (e){
  e.preventDefault();
  
  $.ajax({
    type: 'POST',
    url: order_url,
    dataType: 'json',
    data: {
      first_name: $('#first_name').val(),
      last_name: $('#last_name').val(),
      email: $('#email').val(),
      phone: $('#phone').val(),
      address1: $('#address1').val(),
      address2: $('#address2').val(),
      city: $('#city').val(),
      province: $('#province').val(),
      post_code: $('#zip_code').val(),
      shop: shop,
      csrfmiddlewaretoken: getCookie('csrftoken'),
      action: "post",
    },
    success: function (response) {
      console.log(response.order)
      // window.location.replace("http://127.0.0.1:8000/order/confirmation/");
      paymentForm.classList.add("not-visible");
      eftAlert.classList.add("not-visible");
      breadCrumb.classList.add("not-visible");
      
      
      orderConfirmation.innerHTML += `
        <p class="lead" style="color: #D9AE79 !important;">Thank you, <br> Your order will be processed soon as we recieve payment. 
        Please find further details in your email.</p>

      
        <p class="" style="font-size: 14px;">
          <strong>Order Number (Reference):</strong> ${response.order} <br>
          <strong>Date:</strong> ${response.date} <br>
          <strong>Total:</strong> R${response.total}</br>
          <strong>Payment Method:</strong> EFT
        
        </p> 
        <hr>

        <p class="fw-lighter mt-3">Please note your order will be deleted automatically after 2 days if no payment is made, <br><br> Thank you.</p>
      `
      document.getElementById("cart-quantity").innerHTML = response.cart_quantity;
      
    },
    error: function (xhr, errmsg, err) {},
  })
})




