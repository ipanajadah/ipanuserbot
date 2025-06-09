from PyroUbot import *
from datetime import datetime, timedelta

#Callback handler untuk tombol free trial
@PY.CALLBACK("Cekid_ubot")
async def free_trial_callback(client, callback_query):
    user_id = callback_query.from_user.id

    # Cek apakah user sudah pernah mendapat premium gratis
    free_users = await get_list_from_vars(client.me.id, "CEKID_USER_bot")
    if user_id in free_users:
        return await callback_query.answer("first name: {first_name}\nlast name: {last_name}\nusername: {username}\ndc id: {dc_id}\n", show_alert=True)

    # Tambahkan 1 hari premium
    now = datetime.now(timezone("Asia/Jakarta"))
    expired = now + timedelta(hours=5)

    await set_expired_date(user_id, expired)
    await add_to_vars(client.me.id, "PREM_USERS", user_id)
    await add_to_vars(client.me.id, "FREE_PREM_USERS", user_id)

    # Kirim pesan ke user dengan status free trial
    await callback_query.answer("first name: {first_name}\nlast name: {last_name}\nusername: {username}\ndc id: {dc_id}\n", show_alert=True)
    
    # Kirim pesan dengan tombol inline    
    await bot.send_message(
        user_id,
        f"""
<blockquote><b>
first name: {first_name}
last name: {last_name}
 username: {username}
dc id: {dc_id}</b></blockquote>
""",
  )
  
