$(function() {
  $("#threadBoard").change(function() {
    $("#replyBoard").val($("#threadBoard").val());
  });

  $("#replyBoard").change(function() {
    $("#threadBoard").val($("#replyBoard").val());
  });

  function getFormDataObject(formId) {
    return $("#" + formId)
      .serializeArray()
      .reduce(function(object, item) {
        object[item.name] = item.value;
        return object;
      }, {});
  }

  function displayResult(result) {
    $("#apiOutput").text(JSON.stringify(result, null, 2));
    hljs.highlightBlock(document.getElementById("apiOutput"));
    $("#apiOutputModal").modal("show");
  }

  $("#addNewThread").submit(function() {
    event.preventDefault();
    if ($("#threadBoard").val()) {
      $("button").attr("disabled", true);
      $("button", this).html(
        '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span><span class="sr-only">Uploading...</span>'
      );
      $.ajax({
        url: "/api/threads/" + $("#threadBoard").val(),
        type: "post",
        dataType: "json",
        data: getFormDataObject("addNewThread"),
        success: function(result) {
          displayResult(result);
          $("#addNewThread button").html("POST");
          $("button").removeAttr("disabled");
        },
        error: function() {
          window.location.href =
            "https://message-board-python.tymick.me/b/" +
            $("#threadBoard").val();
        }
      });
    } else {
      $("#threadBoard").focus();
    }
  });

  $("#getRecentThreads").submit(function() {
    event.preventDefault();
    if ($("#threadBoard").val()) {
      $("button").attr("disabled", true);
      $("button", this).html(
        '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span><span class="sr-only">Uploading...</span>'
      );
      $.ajax({
        url: "/api/threads/" + $("#threadBoard").val(),
        type: "get",
        success: function(result) {
          displayResult(result);
          $("#getRecentThreads button").html("GET");
          $("button").removeAttr("disabled");
        }
      });
    } else {
      $("#threadBoard").focus();
    }
  });

  $("#reportThread").submit(function() {
    event.preventDefault();
    if ($("#threadBoard").val()) {
      $("button").attr("disabled", true);
      $("button", this).html(
        '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span><span class="sr-only">Uploading...</span>'
      );
      $.ajax({
        url: "/api/threads/" + $("#threadBoard").val(),
        type: "put",
        data: getFormDataObject("reportThread"),
        success: function(result) {
          displayResult(result);
          $("#reportThread button").html("PUT");
          $("button").removeAttr("disabled");
        }
      });
    } else {
      $("#threadBoard").focus();
    }
  });

  $("#deleteThread").submit(function() {
    event.preventDefault();
    if ($("#threadBoard").val()) {
      $("button").attr("disabled", true);
      $("button", this).html(
        '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span><span class="sr-only">Uploading...</span>'
      );
      $.ajax({
        url: "/api/threads/" + $("#threadBoard").val(),
        type: "delete",
        data: getFormDataObject("deleteThread"),
        success: function(result) {
          displayResult(result);
          $("#deleteThread button").html("DELETE");
          $("button").removeAttr("disabled");
        }
      });
    } else {
      $("#threadBoard").focus();
    }
  });

  $("#addNewReply").submit(function() {
    event.preventDefault();
    if ($("#replyBoard").val()) {
      $("button").attr("disabled", true);
      $("button", this).html(
        '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span><span class="sr-only">Uploading...</span>'
      );
      $.ajax({
        url: "/api/replies/" + $("#replyBoard").val(),
        type: "post",
        data: getFormDataObject("addNewReply"),
        dataType: "json",
        success: function(result) {
          displayResult(result);
          $("#addNewReply button").html("POST");
          $("button").removeAttr("disabled");
        },
        error: function() {
          window.location.href =
            "https://message-board-python.tymick.me/b/" +
            $("#replyBoard").val() +
            "/" +
            $("#postReplyThreadId").val();
        }
      });
    } else {
      $("#replyBoard").focus();
    }
  });

  $("#getThreadAndReplies").submit(function() {
    event.preventDefault();
    if ($("#replyBoard").val()) {
      $("button").attr("disabled", true);
      $("button", this).html(
        '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span><span class="sr-only">Uploading...</span>'
      );
      $.ajax({
        url: "/api/replies/" + $("#replyBoard").val(),
        type: "get",
        data: $("#getThreadAndReplies").serialize(),
        success: function(result) {
          displayResult(result);
          $("#getThreadAndReplies button").html("GET");
          $("button").removeAttr("disabled");
        }
      });
    } else {
      $("#replyBoard").focus();
    }
  });

  $("#reportReply").submit(function() {
    event.preventDefault();
    if ($("#replyBoard").val()) {
      $("button").attr("disabled", true);
      $("button", this).html(
        '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span><span class="sr-only">Uploading...</span>'
      );
      $.ajax({
        url: "/api/replies/" + $("#replyBoard").val(),
        type: "put",
        data: getFormDataObject("reportReply"),
        success: function(result) {
          displayResult(result);
          $("#reportReply button").html("PUT");
          $("button").removeAttr("disabled");
        }
      });
    } else {
      $("#replyBoard").focus();
    }
  });

  $("#deleteReply").submit(function() {
    event.preventDefault();
    if ($("#replyBoard").val()) {
      $("button").attr("disabled", true);
      $("button", this).html(
        '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span><span class="sr-only">Uploading...</span>'
      );
      $.ajax({
        url: "/api/replies/" + $("#replyBoard").val(),
        type: "delete",
        data: getFormDataObject("deleteReply"),
        success: function(result) {
          displayResult(result);
          $("#deleteReply button").html("DELETE");
          $("button").removeAttr("disabled");
        }
      });
    } else {
      $("#replyBoard").focus();
    }
  });
});
