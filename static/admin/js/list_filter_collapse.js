/**
 * Created by reedd on 9/13/17.
 */
// Fancier version https://gist.github.com/985283

;(function($){ $(document).ready(function(){
    $('#changelist-filter').children('h3').each(function(){
        var $title = $(this);
        $title.click(function(){
            $title.next().slideToggle();
        });
    });
  });
})(django.jQuery);