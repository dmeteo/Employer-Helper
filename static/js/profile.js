const profileInfoForm = document.querySelector('.profile-info-form');
const editInfoButton = document.querySelector('.profile-info-edit-button');
const cancelInfoButton = document.querySelector('.profile-info-cancel-button');
const saveInfoButton = document.querySelector('.profile-info-save-button');
const profileInfoInputs = document.querySelectorAll('.profile-info-input');

editInfoButton.addEventListener('click', function() {
    for (let i = 0; i < profileInfoInputs.length; i++) {
        profileInfoInputs[i].readOnly = false;
    }
    profileInfoInputs[5].disabled = false;

    editInfoButton.hidden = true;
    cancelInfoButton.hidden = false;
    saveInfoButton.hidden = false;
});

cancelInfoButton.addEventListener('click', function() {
    /* Cancel changes */
    for (let i = 0; i < profileInfoInputs.length; i++) {
        profileInfoInputs[i].readOnly = true;
    }
    profileInfoInputs[5].disabled = true;

    editInfoButton.hidden = false;
    cancelInfoButton.hidden = true;
    saveInfoButton.hidden = true;
});

profileInfoForm.addEventListener('submit', function(evt) {
    for (let i = 0; i < profileInfoInputs.length; i++) {
        profileInfoInputs[i].readOnly = true;
    }
    profileInfoInputs[5].disabled = true;
    
    editInfoButton.hidden = false;
    cancelInfoButton.hidden = true;
    saveInfoButton.hidden = true;
})

