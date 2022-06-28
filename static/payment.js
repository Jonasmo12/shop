//'use strict';
var payment_url = document.location.href
console.log('payment url: ', payment_url)


// function getCookie(name) {
//   let cookieValue = null;
//   if (document.cookie && document.cookie !== "") {
//     const cookies = document.cookie.split(";");
//     for (let i = 0; i < cookies.length; i++) {
//       const cookie = cookies[i].trim();
//       // Does this cookie string begin with the name we want?
//       if (cookie.substring(0, name.length + 1) === (name + "=")) {
//         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//         break;
//       }
//     }
//   }
//   return cookieValue;
// }

// Replace the supplied `publicKey` with your own.
// Ensure that in production you use a production public_key.
var sdk = new window.YocoSDK({
  publicKey: 'pk_test_eacbf366AVOLmKo62094'
});

console.log(cartTotal)
console.log(sdk.inline.customer)
// Create a new dropin form instance
var inline = sdk.inline({
  layout: 'basic',
  amountInCents: cartTotal,
  currency: 'ZAR',
  // customer.email: $('#email').val(),
});

// this ID matches the id of the element we created earlier.
inline.mount('#card-frame');


// Run our code when your form is submitted
var form = document.getElementById('payment-form');
var submitButton = document.getElementById('pay-button');
form.addEventListener('submit', function (event) {
  event.preventDefault()
  // Disable the button to prevent multiple clicks while processing
  submitButton.disabled = true;
  // This is the inline object we created earlier with the sdk
  inline.createToken().then(function (result) {
    // Re-enable button now that request is complete
    // (i.e. on success, on error and when auth is cancelled)
    submitButton.disabled = false;
    if (result.error) {
      const errorMessage = result.error.message;
      errorMessage && alert("error occured: " + errorMessage);
    } else {
      const token = result;
      alert("card successfully tokenised: " + token.id);
    }
  }).catch(function (error) {
    // Re-enable button now that request is complete
    submitButton.disabled = false;
    alert("error occured: " + error);
  });
});
// Any additional form data you want to submit to your backend should be done here, or in another event listener


var first_name = document.getElementById('first_name')
console.log(first_name)

inline.on('card_tokenized', function (event) {
  // Code to handle the event goes here
  console.log('post to backend');
  console.log('token_id:', event.id)

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
      token_id: event.id,
      csrfmiddlewaretoken: CSRF_TOKEN,
      action: "post",
    },
    success: function (json) {
      console.log(json.success)
      window.location.replace("http://127.0.0.1:8000/payment/orderplaced/");
    },
    error: function (xhr, errmsg, err) {},
  })
});

// form.addEventListener('submit', function (event) {
//   event.preventDefault()
  
//   $.ajax({
//     type: "POST",
//     url: 'http://127.0.0.1/order/add',
//     data: {
//       csrfmiddlewaretoken: CSRF_TOKEN,
//       action: "post",
//     },
//     success: function (json) {
//       console.log(json.success)
  
//       // stripe.confirmCardPayment(clientsecret, {
//       //   payment_method: {
//       //     card: card,
//       //     billing_details: {
//       //       address:{
//       //           line1:custAdd,
//       //           line2:custAdd2
//       //       },
//       //       name: custName
//       //     },
//       //   }
//       // }).then(function(result) {
//       //   if (result.error) {
//       //     console.log('payment error')
//       //     console.log(result.error.message);
//       //   } else {
//       //     if (result.paymentIntent.status === 'succeeded') {
//       //       console.log('payment processed')
//       //       // There's a risk of the customer closing the window before callback
//       //       // execution. Set up a webhook or plugin to listen for the
//       //       // payment_intent.succeeded event that handles any business critical
//       //       // post-payment actions.
//       //       window.location.replace("http://127.0.0.1:8000/payment/orderplaced/");
//       //     }
//       //   }
//       // });
  
//     },
//     error: function (xhr, errmsg, err) {},
//   });
  
// })


