$(function() {
    String.prototype.capitalize = function() {
        return this.charAt(0).toUpperCase() + this.slice(1);
    };

    var $body = $('body');
    var language_code = $body.data('language-code');
    var event_src = $body.data('event-src');
    var tpl_path = $body.data('tpl-path');

    var calendar = $('#calendar').calendar({
        language: language_code,
        view: 'month',
        events_source: event_src,
        tmpl_path: tpl_path,
        tmpl_cache: false,
        modal: '#events-modal',
        time_start: '12:00',
		time_end: '24:00',
		time_split: '30',
        modal_type : 'ajax',
        modal_title: function(event) {
            return event.title
        },
		onAfterViewLoad: function(view) {
            $('#cal_title').text(this.getTitle().capitalize());
			$('.btn-group button').removeClass('active');
			$('button[data-calendar-view="' + view + '"]').addClass('active');
		},
		classes: {
			months: {
				general: 'label'
			}
		}
    });
	$('.btn-group button[data-calendar-nav]').each(function() {
		var $this = $(this);
		$this.click(function() {
			calendar.navigate($this.data('calendar-nav'));
		});
	});
	$('.btn-group button[data-calendar-view]').each(function() {
		var $this = $(this);
		$this.click(function() {
			calendar.view($this.data('calendar-view'));
		});
	});
});
