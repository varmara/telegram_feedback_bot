start-text = 
    Hello { $user_full_name }!
    This bot collects content suggestions for a telegram channel. 
    Write a message and it will be forwarded to the editors.

help-text-user =
    /start - start the bot
    /help - show help

help-text-admin =
    /whois - получить информацию о пользователе
    /ban - забанить пользователя
    /unban - разбанить пользователя
    /help - показать помощь

message-from = 
    <a href='tg://user?id={ $user_id }'>{ $user_full_name }</a> (@{ $username }) { $admin_time() }
    { $formatted_message }

thank-you-message-accepted =
    Thank you! Your message is accepted.

error-send-message = 
    Error sending message.

error-unsupported-message-type = 
    Error. Message type is not supported.

command-help-description-user = 
    Bot usage guide.

command-help-description-admin = 
    Admin commands.

command-start-description = 
    Start the bot.

command-whois-description
    Get user info.

command-ban-description
    Ban user.

command-unban-description
    Unban user.
