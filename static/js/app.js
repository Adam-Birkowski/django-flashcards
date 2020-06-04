$("form").keypress(function(e) {
    //Enter key
    if (e.which == 13) {
      return false;
    }
  });

  console.log($("form"));