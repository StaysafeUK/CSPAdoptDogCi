const editButtons = document.getElementsByClassName("btn-edit");
const leavecommentText = document.getElementById("id_body");
const leavecommentForm = document.getElementById("leavecommentForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated leavecomment's ID upon click.
* - Fetches the content of the corresponding leavecomment.
* - Populates the `leavecommentText` input/textarea with the leavecomment's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_leavecomment/{leavecommentId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let leavecommentId = e.target.getAttribute("leavecomment_id");
    let leavecommentContent = document.getElementById(`leavecomment${leavecommentId}`).innerText;
    leavecommentText.value = leavecommentContent;
    submitButton.innerText = "Update";
    leavecommentForm.setAttribute("action", `edit_leavecomment/${leavecommentId}`);
  });
}

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated leavecomment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific leavecomment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let leavecommentId = e.target.getAttribute("leavecomment_id");
      deleteConfirm.href = `delete_leavecomment/${leavecommentId}`;
      deleteModal.show();
    });
}