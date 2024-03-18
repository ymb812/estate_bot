from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Column, Url, SwitchTo, Select
from core.states.main_menu import MainMenuStateGroup
from core.utils.texts import _
from core.dialogs.custom_content import CustomPager
from core.dialogs.callbacks import CallBackHandler
from core.dialogs.getters import get_categories
from settings import settings


main_menu_dialog = Dialog(
    # menu
    Window(
        Const(text=_('PICK_CATEGORY')),
        Column(
            SwitchTo(Const(text=_('GAB_BUTTON')), id='go_to_gab', state=MainMenuStateGroup.gab),
            SwitchTo(Const(text=_('ESTATE_BUTTON')), id='go_to_commercial', state=MainMenuStateGroup.commercial),
            Url(
                Const(text=_('SUPPORT_BUTTON')),
                Const(text=settings.admin_chat_link),
            )
        ),
        state=MainMenuStateGroup.menu,
    ),

    # budget
    Window(
        Const(text=_('PICK_BUDGET')),
        CustomPager(
            Select(
                id='_budget_select',
                items='budgets',
                item_id_getter=lambda item: item.id,
                text=Format(text='{item.name}'),
                on_click=CallBackHandler.selected_content,
            ),
            id='budget_group',
            height=settings.categories_per_page_height,
            width=settings.categories_per_page_width,
            hide_on_single_page=True,
        ),
        SwitchTo(Const(text=_('BACK_BUTTON')), id='go_to_menu', state=MainMenuStateGroup.menu),
        getter=get_categories,
        state=MainMenuStateGroup.gab,
    ),

    # commercial
    Window(
        Const(text=_('PICK_COMMERCIAL')),
        CustomPager(
            Select(
                id='_commercial_select',
                items='commercial',
                item_id_getter=lambda item: item.id,
                text=Format(text='{item.name}'),
                on_click=CallBackHandler.selected_content,
            ),
            id='budget_group',
            height=settings.categories_per_page_height,
            width=settings.categories_per_page_width,
            hide_on_single_page=True,
        ),
        SwitchTo(Const(text=_('BACK_BUTTON')), id='go_to_menu', state=MainMenuStateGroup.menu),
        getter=get_categories,
        state=MainMenuStateGroup.commercial,
    ),
)
