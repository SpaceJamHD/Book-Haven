$(document).ready(function() {
    $('#feedback-form').submit(function(event) {
        event.preventDefault(); // Prevent default form submission

        var formData = $(this).serialize(); // Serialize form data
        $.ajax({
            url: $(this).attr('action'), // Form action URL
            type: 'POST',
            data: formData,
            success: function(response) {
                console.log(response); // Log the response to see its structure
                // Check if response indicates success
                if (response.success) {
                    console.log('Comment submitted successfully');
                    // Clear the comment textarea
                    $('#id_comment').val('');
                    // Add the new comment to the comments list
                    var newCommentHtml = '<li>' +
                        response.user + ' написал(а) ' + response.created_at + ':<br />' +
                        response.comment +
                        '</li>';
                    $('#comments-list').append(newCommentHtml);
                } else {
                    console.error('Error submitting comment');
                }
            },
            error: function(xhr, textStatus, errorThrown) {
                console.error('Error submitting comment:', errorThrown);
            }
        });
    });
});
