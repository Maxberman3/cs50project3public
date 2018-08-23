$(document).ready( function(){
  const $totalspan=$('#total');
  $('.btn-danger').each( function(){
   $(this).click(function(){
     const value=$(this).val();
     item={
       item_id:value,
       current_total:$totalspan.html(),
     };
     $.ajax({
       type:'POST',
       url:'http://127.0.0.1:8000/merch/cartremove',
       data:item,
       success:function(data){
         $('#'+value).hide();
         $totalspan.html(data['newtotal']);
       },
     });
   });
  });
});
