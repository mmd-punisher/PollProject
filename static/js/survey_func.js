/*  Wizard */
jQuery(function ($) {
	"use strict";
	$('form#wrapped').attr('action', 'level2.html');
	$("#wizard_container").wizard({
		stepsWrapper: "#wrapped",
		submit: ".submit",
		beforeSelect: function (event, state) {
			if ($('input#website').val().length != 0) {
				return false;
			}
			if (!state.isMovingForward)
				return true;
			var inputs = $(this).wizard('state').step.find(':input');
			return !inputs.length || !!inputs.valid();
		}
	}).validate({
		errorPlacement: function (error, element) {
			if (element.is(':radio') || element.is(':checkbox')) {
				error.insertBefore(element.next());
			} else {
				error.insertAfter(element);
			}
		}
	});
	//  progress bar
	$("#progressbar").progressbar();
	$("#wizard_container").wizard({
		afterSelect: function (event, state) {
			$("#progressbar").progressbar("value", state.percentComplete);
			$("#location").text("(" + state.stepsComplete + "/" + state.stepsPossible + ")");
		}
	});
	// Validate select
	$('#wrapped').validate({
		ignore: [],
		rules: {
			select: {
				required: true
			}
		},
		errorPlacement: function (error, element) {
			if (element.is('select:hidden')) {
				error.insertAfter(element.next('.nice-select'));
			} else {
				error.insertAfter(element);
			}
		}
	});
});

// Summary 
function getVals(formControl, controlType) {
	switch (controlType) {

		case 'question_1':
			// Get the value for a radio
			var value = $(formControl).val();
			$("#question_1").text(value);
			break;

		case 'question_2':
			// Get the value for a radio
			var value = $(formControl).val();
			$("#question_2").text(value);
			break;
		case 'question_3':
			// Get the value for a radio
			var value = $(formControl).val();
			$("#question_3").text(value);
			break;
		case 'question_4':
			// Get the value for a radio
			var value = $(formControl).val();
			$("#question_4").text(value);
			break;
		case 'question_5':
			// Get the value for a radio
			var value = $(formControl).val();
			$("#question_5").text(value);
			break;
		case 'question_6':
			// Get the value for a radio
			var value = $(formControl).val();
			$("#question_6").text(value);
			break;
		case 'question_7':
			// Get the value for a radio
			var value = $(formControl).val();
			$("#question_7").text(value);
			break;
		case 'question_8':
			// Get the value for a radio
			var value = $(formControl).val();
			$("#question_8").text(value);
			break;
		case 'question_9':
			// Get the value for a radio
			var value = $(formControl).val();
			$("#question_9").text(value);
			break;
		case 'question_10':
			// Get the value for a radio
			var value = $(formControl).val();
			$("#question_10").text(value);
			break;
		case 'question_11':
			// Get the value for a radio
			var value = $(formControl).val();
			$("#question_11").text(value);
			break;
		case 'question_12':
			// Get the value for a radio
			var value = $(formControl).val();
			$("#question_12").text(value);
			break;
		case 'question_13':
			// Get the value for a radio
			var value = $(formControl).val();
			$("#question_13").text(value);
			break;
		case 'question_14':
			// Get the value for a radio
			var value = $(formControl).val();
			$("#question_14").text(value);
			break;
		case 'question_15':
			// Get the value for a radio
			var value = $(formControl).val();
			$("#question_15").text(value);
			break;
		case 'question_16':
			// Get the value for a radio
			var value = $(formControl).val();
			$("#question_16").text(value);
			break;
		case 'question_17':
			// Get the value for a radio
			var value = $(formControl).val();
			$("#question_17").text(value);
			break;

	}
}