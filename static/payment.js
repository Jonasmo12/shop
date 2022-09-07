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

    },
    error: function (xhr, errmsg, err) {},
  })
})




