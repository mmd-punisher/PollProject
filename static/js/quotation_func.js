	/*  Wizard */
	jQuery(function ($) {
		"use strict";
		$('form#wrapped').attr('action', 'quotation.php');
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

/* File upload validate size and file type - For details: https://github.com/snyderp/jquery.validate.file*/
		$("form#wrapped")
			.validate({
				rules: {
					fileupload: {
						fileType: {
							types: ["jpg", "jpeg", "gif", "png", "pdf"]
						},
						maxFileSize: {
							"unit": "KB",
							"size": 50
						},
						minFileSize: {
							"unit": "KB",
							"size": "2"
						}
					}
				}
			});
// Summary 
function getVals(formControl, controlType) {
	switch (controlType) {

		case 'question_1':
			// Get name for set of checkboxes
			var checkboxName = $(formControl).attr('name');

			// Get all checked checkboxes
			var value = [];
			$("input[name*='" + checkboxName + "']").each(function () {
				// Get all checked checboxes in an array
				if (jQuery(this).is(":checked")) {
					value.push($(this).val());
				}
			});
			$("#question_1").text(value.join(", "));
			break;

		case 'additional_message':
			// Get the value for a textarea
			var value = $(formControl).val();
			$("#additional_message").text(value);
			break;
            
         case 'fileupload':
			// Get the value for a textarea
			var value = $(formControl).val();
			$("#fileupload").text(value);
			break;
        
        case 'budget':
			// Get the value for a textarea
			var value = $(formControl).val();
			$("#budget").text(value);
			break;
	}
}