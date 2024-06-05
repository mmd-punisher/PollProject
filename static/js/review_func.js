/*  Wizard */
jQuery(function ($) {
	"use strict";
	$('form#wrapped').attr('action',);
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

		case 'rating_input_1':
			// Get the value for a input text
			var value = $(formControl).val();
			$("#rating_input_1").text(value);
			break;

		case 'rating_input_2':
			// Get the value for a input text
			var value = $(formControl).val();
			$("#rating_input_2").text(value);
			break;

		case 'rating_input_3':
			// Get the value for a input text
			var value = $(formControl).val();
			$("#rating_input_3").text(value);
			break;

		case 'rating_input_4':
			// Get the value for a select
			var value = $(formControl).val();
			$("#rating_input_4").text(value);
			break;

		case 'review_message':
			// Get the value for a select
			var value = $(formControl).val();
			$("#review_message").text(value);
			break;

	}
}
//neck
function ShowNeck() {
	var choice = document.querySelector('input[name="question_neck"]:checked').value;
	var additionalQuestion = document.getElementById("ShowNeck");

	if (choice === "0") {
		additionalQuestion.classList.add("hidden");
	} else {
		additionalQuestion.classList.remove("hidden");
	}
}

//right_shoulder
function ShowRshoulder() {
	var choice = document.querySelector('input[name="question_Rshoulder"]:checked').value;
	var additionalQuestion = document.getElementById("Rshoulder");

	if (choice === "0") {
		additionalQuestion.classList.add("hidden");
	} else {
		additionalQuestion.classList.remove("hidden");
	}
}
//left_shoulder
function ShowLshoulder() {
	var choice = document.querySelector('input[name="question_Lshoulder"]:checked').value;
	var additionalQuestion = document.getElementById("Lshoulder");

	if (choice === "0") {
		additionalQuestion.classList.add("hidden");
	} else {
		additionalQuestion.classList.remove("hidden");
	}
}
//UBack
function ShowUBack() {
	var choice = document.querySelector('input[name="question_UBack"]:checked').value;
	var additionalQuestion = document.getElementById("UBack");

	if (choice === "0") {
		additionalQuestion.classList.add("hidden");
	} else {
		additionalQuestion.classList.remove("hidden");
	}
}
//back
function ShowBack() {
	var choice = document.querySelector('input[name="question_Back"]:checked').value;
	var additionalQuestion = document.getElementById("Back");

	if (choice === "0") {
		additionalQuestion.classList.add("hidden");
	} else {
		additionalQuestion.classList.remove("hidden");
	}
}

//hip
function ShowHip() {
	var choice = document.querySelector('input[name="question_Hip"]:checked').value;
	var additionalQuestion = document.getElementById("Hip");

	if (choice === "0") {
		additionalQuestion.classList.add("hidden");
	} else {
		additionalQuestion.classList.remove("hidden");
	}
}
//Rmuscle
function ShowRmuscle() {
	var choice = document.querySelector('input[name="question_Rmuscle"]:checked').value;
	var additionalQuestion = document.getElementById("Rmuscle");

	if (choice === "0") {
		additionalQuestion.classList.add("hidden");
	} else {
		additionalQuestion.classList.remove("hidden");
	}
}
//Lmuscle
function ShowLmuscle() {
	var choice = document.querySelector('input[name="question_Lmuscle"]:checked').value;
	var additionalQuestion = document.getElementById("Lmuscle");

	if (choice === "0") {
		additionalQuestion.classList.add("hidden");
	} else {
		additionalQuestion.classList.remove("hidden");
	}
}
//Rforearm
function ShowRforearm() {
	var choice = document.querySelector('input[name="question_Rforearm"]:checked').value;
	var additionalQuestion = document.getElementById("Rforearm");

	if (choice === "0") {
		additionalQuestion.classList.add("hidden");
	} else {
		additionalQuestion.classList.remove("hidden");
	}
}
//Lforearm
function ShowLforearm() {
	var choice = document.querySelector('input[name="question_Lforearm"]:checked').value;
	var additionalQuestion = document.getElementById("Lforearm");

	if (choice === "0") {
		additionalQuestion.classList.add("hidden");
	} else {
		additionalQuestion.classList.remove("hidden");
	}
}
//RWrist
function ShowRWrist() {
	var choice = document.querySelector('input[name="question_RWrist"]:checked').value;
	var additionalQuestion = document.getElementById("RWrist");

	if (choice === "0") {
		additionalQuestion.classList.add("hidden");
	} else {
		additionalQuestion.classList.remove("hidden");
	}
}

//LWrist
function ShowLWrist() {
	var choice = document.querySelector('input[name="question_LWrist"]:checked').value;
	var additionalQuestion = document.getElementById("LWrist");

	if (choice === "0") {
		additionalQuestion.classList.add("hidden");
	} else {
		additionalQuestion.classList.remove("hidden");
	}
}

//Rthing
function ShowRthing() {
	var choice = document.querySelector('input[name="question_Rthing"]:checked').value;
	var additionalQuestion = document.getElementById("Rthing");

	if (choice === "0") {
		additionalQuestion.classList.add("hidden");
	} else {
		additionalQuestion.classList.remove("hidden");
	}
}

//Lthing
function ShowLthing() {
	var choice = document.querySelector('input[name="question_Lthing"]:checked').value;
	var additionalQuestion = document.getElementById("Lthing");

	if (choice === "0") {
		additionalQuestion.classList.add("hidden");
	} else {
		additionalQuestion.classList.remove("hidden");
	}
}
//RLeg
function ShowRLeg() {
	var choice = document.querySelector('input[name="question_RLeg"]:checked').value;
	var additionalQuestion = document.getElementById("RLeg");

	if (choice === "0") {
		additionalQuestion.classList.add("hidden");
	} else {
		additionalQuestion.classList.remove("hidden");
	}
}
//LLeg
function ShowLLeg() {
	var choice = document.querySelector('input[name="question_LLeg"]:checked').value;
	var additionalQuestion = document.getElementById("LLeg");

	if (choice === "0") {
		additionalQuestion.classList.add("hidden");
	} else {
		additionalQuestion.classList.remove("hidden");
	}
}
//RKnee
function ShowRKnee() {
	var choice = document.querySelector('input[name="question_RKnee"]:checked').value;
	var additionalQuestion = document.getElementById("RKnee");

	if (choice === "0") {
		additionalQuestion.classList.add("hidden");
	} else {
		additionalQuestion.classList.remove("hidden");
	}
}
//LKnee
function ShowLKnee() {
	var choice = document.querySelector('input[name="question_LKnee"]:checked').value;
	var additionalQuestion = document.getElementById("LKnee");

	if (choice === "0") {
		additionalQuestion.classList.add("hidden");
	} else {
		additionalQuestion.classList.remove("hidden");
	}
}
//Rsole
function ShowRsole() {
	var choice = document.querySelector('input[name="question_Rsole"]:checked').value;
	var additionalQuestion = document.getElementById("Rsole");

	if (choice === "0") {
		additionalQuestion.classList.add("hidden");
	} else {
		additionalQuestion.classList.remove("hidden");
	}
}
//Lsole
function ShowLsole() {
	var choice = document.querySelector('input[name="question_Lsole"]:checked').value;
	var additionalQuestion = document.getElementById("Lsole");

	if (choice === "0") {
		additionalQuestion.classList.add("hidden");
	} else {
		additionalQuestion.classList.remove("hidden");
	}
}
document.addEventListener('DOMContentLoaded', function() {
    const ageInput = document.querySelector('#age-container input[name="age"]');

    ageInput.addEventListener('input', function() {
        const age = parseInt(ageInput.value, 10);

        if (isNaN(age) || age < 10 || age > 90) {
            ageInput.classList.add('error');
        } else {
            ageInput.classList.remove('error');
        }
    });
});