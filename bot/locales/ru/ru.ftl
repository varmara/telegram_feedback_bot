start-text = 
    Здравствуйте, { $user_full_name }!
    Это бот для сбора предложений для канала. 
    Напишите сообщение, и оно будет переправлено редакторам.

help-text-user =
    /start - начать работу
    /help - показать помощь

help-text-admin =
    /whois - получить информацию о пользователе
    /ban - забанить пользователя
    /unban - разбанить пользователя
    /help - показать помощь

message-from = 
    <a href='tg://user?id={ $user_id }'>{ $user_full_name }</a> (@{ $username }) { $admin_time() }
    { $formatted_message }

thank-you-message-accepted =
    Спасибо! Ваше сообщение принято.

error-send-message = 
    Ошибка при отправке сообщения.

error-unsupported-message-type = 
    Ошибка. Тип сообщения не поддерживается.

command-help-description-user = 
    Справка о работе бота.

command-help-description-admin = 
    Команды администратора.

command-start-description = 
    Начать работу.

command-whois-description
    Получить информацию о пользователе.

command-ban-description
    Забанить пользователя.

command-unban-description
    Разбанить пользователя.
