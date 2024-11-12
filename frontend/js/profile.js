profileInfoForm = document.querySelector('.profile-info');
editInfoButton = document.querySelector('.profile-info-edit-button');
canselInfoButton = document.querySelector('.profile-info-cansel-button');
saveInfoButton = document.querySelector('.profile-info-save-button');
profileInfoInputs = document.querySelectorAll('.profile-info-input');

editInfoButton.addEventListener('click', function() {
    for (let i = 0; i < profileInfoInputs.length; i++) {
        profileInfoInputs[i].readonly = false;
    }
    editInfoButton.hidden = true;
    canselInfoButton.hidden = false;
    saveInfoButton.hidden = false;
});

canselInfoButton.addEventListener('click', function() {
    /* Cancel changes */
    for (let i = 0; i < profileInfoInputs.length; i++) {
        profileInfoInputs[i].readonly = true;
    }
    editInfoButton.hidden = false;
    canselInfoButton.hidden = true;
    saveInfoButton.hidden = true;
});

saveInfoButton.addEventListener('click', function() {
    for (let i = 0; i < profileInfoInputs.length; i++) {
        profileInfoInputs[i].readonly = true;
    }
    editInfoButton.hidden = false;
    canselInfoButton.hidden = true;
    saveInfoButton.hidden = true;
});

profileInfoForm.addEventListener('submit', function(evt) {
    /* Save changes */
})