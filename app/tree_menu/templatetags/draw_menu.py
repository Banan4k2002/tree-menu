from django import template

from tree_menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('tree_menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu):
    selected_item_pk = context['request'].GET.get(menu)
    items = MenuItem.objects.filter(menu__title=menu).select_related(
        'parent_item'
    )
    items_dict = {item.pk: item for item in items}
    tree = build_tree(items, items_dict)

    context_data = {
        'tree': tree,
        'menu': menu,
    }

    if selected_item_pk:
        selected_item = items_dict.get(int(selected_item_pk))
        if selected_item:
            context_data['parents'] = get_parents(selected_item, items_dict)

    return context_data


def get_parents(item, items_dict):
    """Возвращает список родительских элементов для данного элемента."""
    parents = []
    while item.parent_item:
        parents.append(item)
        item = items_dict.get(item.parent_item_id)
    parents.append(item)
    return parents


def build_tree(items, items_dict):
    """Возвращает корневые элементы с иерархической структурой."""
    tree = []
    for item in items:
        if item.parent_item:
            parent = items_dict[item.parent_item_id]
            if not hasattr(parent, 'children'):
                parent.children = []
            parent.children.append(item)
        else:
            tree.append(item)
    return tree
