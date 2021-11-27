from aiogram import types

from app.misc import dp
from app.models.Musics import Musics


def get_musics(query, start_num: int):
    _music = Musics(query.query.lower())
    overall_items = _music.Search_Inline_Music(types=True)
    if start_num >= overall_items:
        return []
    else:
        return _music.Search_Inline_Music(offset=start_num)


@dp.inline_handler()
async def query_text(query: types.InlineQuery):
    query_offset = int(query.offset) if query.offset else 0
    username = (await dp.bot.get_me()).username
    results = [
        types.InlineQueryResultCachedAudio(
            id=str(music.id),
            audio_file_id=music.file_id,
            caption=f"🔥 @{username.capitalize()} 👈 <b>больше музыки</b>")
        for music in get_musics(query, query_offset)
    ]
    if len(results) < 50:
        try:
            await query.answer(results, cache_time=0,
                               switch_pm_text="Слушайте больше музыки",
                               switch_pm_parameter='start')
        except:
            pass
    else:
        try:
            await query.answer(results, is_personal=True, next_offset=str(query_offset + 50), cache_time=0,
                               switch_pm_text="Слушайте больше музыки",
                               switch_pm_parameter='start')
        except:
            pass
