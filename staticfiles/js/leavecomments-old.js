// Select all edit buttons and form elements
const editButtons = document.querySelectorAll(".btn-edit");
const leavecommentText = document.getElementById("id_comment");  // Assuming this is the ID of the textarea for comment
const leavecommentForm = document.getElementById("leavecommentForm");
const submitButton = document.getElementById("submitButton");

// Initialize edit functionality for each edit button
editButtons.forEach(button => {
  button.addEventListener("click", (e) => {
    const leavecommentId = e.target.getAttribute("leavecomment_id");
    const leavecommentContent = document.getElementById(`leavecomment${leavecommentId}`).innerText;

    // Populate the comment content into the textarea
    leavecommentText.value = leavecommentContent;

    // Change the submit button text to "Update"
    submitButton.innerText = "Update";

    // Update the form's action attribute to point to the edit URL
    leavecommentForm.setAttribute("action", `/edit_leavecomment/${leavecommentId}/`);

    // Optionally, scroll to the comment form or highlight it
    leavecommentForm.scrollIntoView({ behavior: "smooth" });
  });
});

// Uncomment the deletion functionality if needed
/*
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let leavecommentId = e.target.getAttribute("leavecomment_id");
      deleteConfirm.href = `delete_leavecomment/${leavecommentId}`;
      deleteModal.show();
    });
}
*/
