/* Select all edit buttons and form elements */
const editButtons = document.querySelectorAll(".btn-edit");
const leavecommentText = document.getElementById("id_comment");  // This ID should match the Django form field's ID
const leavecommentForm = document.getElementById("leavecommentForm");
const submitButton = leavecommentForm.querySelector("button[type='submit']");  // Target the submit button within the form

/* Initialize edit for each edit button */
editButtons.forEach(button => {
  button.addEventListener("click", (e) => {
    const leavecommentId = button.getAttribute("comment_id");  // Use comment_id as per the template
    const leavecommentContent = document.getElementById(`leavecomment${leavecommentId}`).innerText.trim();

    /* Populate the comment content into the textarea */
    leavecommentText.value = leavecommentContent;

    /* Change the submit button text to "Update" */
    submitButton.innerText = "Update";
    
    /* test for Form action and display in console.log */
    console.log(`Form action updated to: '/about/edit_leavecomment/${leavecommentId}/`);

    /* Update the form's action attribute to point to the edit URL */
    commentForm.setAttribute("action", `/about/edit_leavecomment/${commentId}/`);


    /* Scroll to the comment form or highlight */
    leavecommentForm.scrollIntoView({ behavior: "smooth" });
  });
});

/* Uncomment the deletion functionality if needed */

const deleteButtons = document.querySelectorAll(".btn-delete");
const deleteModal = new bootstrap.Modal(document.getElementById("leavecommentdeleteModal"));
const deleteConfirm = document.getElementById("deleteConfirmLeaveComment"); // Updated ID

deleteButtons.forEach(button => {
  /* Arrow function for For loop to confirm deletion and show Modal in About.html */
    button.addEventListener("click", (e) => {
        const leavecommentId = button.getAttribute("comment_id");
        deleteConfirm.href = `/about/delete_leavecomment/${leavecommentId}/`; // Updated URL
        deleteModal.show();
    });
});
