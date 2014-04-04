$(document).ready ->
  roomNo = 1
  temp = 20
  
  run = () ->
    $.ajax
      url:'http://localhost:3000/logTemp.json'
      data: { data: [roomNo, temp] }
      type: 'post'
    
    if roomNo >= 4
      roomNo = 1
    else 
      roomNo += 1
    temp += 1
    console.log("run was called!")
  setInterval(run, 3000)
  



  $('#submit').click  ->
    $.ajax
      url:'http://localhost:3000/setTemp.json'
      data: { data: [roomNo, temp] }
      type: 'post'
    # roomNo = $('#roomNo option:selected').text();
    # temp = $('#value').val()
    # $.ajax
    #   url:'http://localhost:3000/getTemp.json'
    #   data: { data: "room#{roomNo}" }
    #   type: 'get'  
    #   dataType:'json'
    #   timeout:3000 
    #   success: (json) ->
    #     alert JSON.stringify json
    #   error: (error) ->
    #     alert JSON.stringify "#{error.status} #{error.statusText}  "

