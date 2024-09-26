// Select all edit buttons and form elements
const editButtons = document.querySelectorAll(".btn-edit");
const leavecommentText = document.getElementById("id_comment");  // Make sure this ID matches the textarea's ID
const leavecommentForm = document.getElementById("leavecommentForm");
const submitButton = leavecommentForm.querySelector("button[type='submit']");  // Target the submit button within the form

// Initialize edit functionality for each edit button
editButtons.forEach(button => {
  button.addEventListener("click", (e) => {
    const leavecommentId = button.getAttribute("comment_id");  // Use comment_id as per the template
    const leavecommentContent = document.getElementById(`leavecomment${leavecommentId}`).innerText.trim();

    // Populate the comment content into the textarea
    leavecommentText.value = leavecommentContent;

    // Change the submit button text to "Update"
    submitButton.innerText = "Update";

    // Update the form's action attribute to point to the edit URL
    leavecommentForm.setAttribute("action", `/edit_leavecomment/${leavecommentId}/`);

    // Scroll to the comment form or highlight it
    leavecommentForm.scrollIntoView({ behavior: "smooth" });
  });
});

// Uncomment the deletion functionality if needed
/*
const deleteButtons = document.querySelectorAll(".btn-delete");
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteConfirm = document.getElementById("deleteConfirm");

deleteButtons.forEach(button => {
    button.addEventListener("click", (e) => {
      const leavecommentId = button.getAttribute("comment_id");
      deleteConfirm.href = `/delete_leavecomment/${leavecommentId}/`;
      deleteModal.show();
    });
});
*/
