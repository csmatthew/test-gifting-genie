$(document).ready(function() {
    $('#search-button').on('click', function() {
        var query = $('#id_friend_username').val();
        if (query.length > 2) {
            $.ajax({
                url: searchUsernamesUrl,
                data: {
                    'term': query
                },
                dataType: 'json',
                success: function(data) {
                    var suggestions = data.map(function(username) {
                        return '<option value="' + username + '">';
                    });
                    $('#username-suggestions').html(suggestions.join(''));
                }
            });
        }
    });
});