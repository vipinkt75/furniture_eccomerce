$(document).ready(function () {
  $('#form').on('submit', function (event) {
    event.preventDefault(); // prevent the form from submitting normally

    $.ajax({
      type: 'POST',
      url: 'contact', // the URL to which the form data will be submitted
      data: $(this).serialize(), // serialize the form data for submission
      dataType: 'json',
      success: function (response) {
        if (response.status === 'true') {
          // if the response indicates success, show the success message
          // $('.sb-success-result').addClass('sb-active');
          swal(
            'Success',
            'message successfully sent',
            'success')
          $('#form').trigger("reset");
        }
        else {
          // if the response indicates failure, show the error message
          
          $(document).on('click', '#ba', function(e) {
            swal(
              'Error!',
              'Form validation error!',
              'error'
            )
            $('#form').trigger("reset");
          });
        }
      },
      // error: function (xhr, textStatus, errorThrown) {
      //   alert('An error occurred while submitting the form.');
      // }
    });
  });
});

// Country Code Selection
$(function() {
  var code = "+91"; // Assigning value from model.
  $('.mobile_codewith_flage').val(code);
  $('.mobile_codewith_flage').intlTelInput({
          autoHideDialCode: true,
          autoPlaceholder: "ON",
          formatOnDisplay: true,
          hiddenInput: "full_number",
          initialCountry: "in",
          nationalMode: true,
          placeholderNumberType: "MOBILE",
          preferredCountries: ['US'],
          separateDialCode: true
  });

  $('.mobilenumber').focusout(function() {
          var code = $(".mobile_codewith_flage").intlTelInput("getSelectedCountryData").dialCode;
          var phoneNumber = $('.phoneNumber').val();
          var name = $(".mobile_codewith_flage").intlTelInput("getSelectedCountryData").name;
          Mobiledata = 'Country Code : ' + code + '\nCountry Name : ' + name + '\nMobile No. :' + phoneNumber;
          var hiddenInput = document.querySelector("input[name='full_number']");
          hiddenInput.value = code;
          document.getElementById('Numbercodeflase').value = Mobiledata;
  });


});


// Add this code after the filter button click event handlers
// $('#apply-filter').on('click', function() {
//   var minPrice = $('#price-slider').slider('getValue')[0];
//   var maxPrice = $('#price-slider').slider('getValue')[1];

//   $.ajax({
//       url: '/filter/',
//       method: 'GET',
//       data: {
//           min_price: minPrice,
//           max_price: maxPrice
//       },
//       success: function(response) {
//           $('.product-item').hide();
//           response.forEach(function(productId) {
//               $('#product-' + productId).show();
//           });
//       },
//       error: function(xhr, status, error) {
//           console.error(error);
//       }
//   });
// });
