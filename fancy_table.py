# coding: utf-8

# # [Fancy Table][1] #

# Dynamic table views for the IPython Notebook
#
# [1]: http://www.snip2code.com/Snippet/47354/Fancy-Table-Using-IPython-Widgets
from math import ceil

from IPython.html import widgets
from IPython.display import display
from IPython.display import display_html, clear_output


def fancy_table(df, step=20, start_cols=None):
    container = widgets.ContainerWidget()
    header = widgets.LatexWidget(value='Columns')
    display(header)
    header.set_css({
        'font-size': '20pt',
        'margin-top': '10pt',
        'margin-bottom': '10pt',
    })
    display(container)

    container.remove_class('vbox')
    container.add_class('hbox')
    container.set_css({
        'width': '100%',
    })
    num_cols = len(df.columns)
    children = [widgets.ContainerWidget()
                for c in range(int(ceil(num_cols / 4.)))]
    for i, c in enumerate(df.columns):
        cc = widgets.ContainerWidget()
        if start_cols is None:
            value = True
        else:
            value = c in start_cols
        box = widgets.CheckboxWidget(value=value, description=c)
        cc.children = [box]
        children[i / 4].children = list(children[i / 4].children) + [cc]
    container.children = children

    def on_click(name, value):
        clear_output(wait=True)
        display_html(df[[c.children[0].description
                         for row in container.children
                         for c in row.children
                         if c.children[0].value is True]])

    row_container = widgets.ContainerWidget()
    header = widgets.LatexWidget(value='Rows')
    display(header)
    header.set_css({
        'font-size': '20pt',
        'margin-top': '10pt',
        'margin-bottom': '10pt',
    })
    display(row_container)
    row_container.remove_class('vbox')
    row_container.add_class('hbox')
    row_filter = widgets.DropdownWidget(values=list(df.columns),
                                        description='filter on')
    query = widgets.TextWidget(value='', description='filter text')
    row_container.children = [row_filter, query]

    page = widgets.IntSliderWidget(value=1, min=1,
                                   max=int(ceil(float(len(df)) / step)))

    def page_table(df):
        if len(df) <= (page.max - 1) * step:
            page.value = 1
        page.max = int(ceil(float(len(df)) / step))
        if len(df) < step:
            display_html(df)
        elif page.value == page.max:
            display_html(df.iloc[(page.value - 1) * step:])
        else:
            display_html(df.iloc[(page.value - 1) * step:page.value * step])

    def on_switch():
        clear_output(wait=True)
        df_c = df[[c.children[0].description
                   for row in container.children
                   for c in row.children
                   if c.children[0].value is True]]
        query_col = df[row_filter.value]
        if query.value in list(query_col):
            df_o = df_c.ix[query_col == query.value]
        else:
            df_o = df_c
        page_table(df_o)

    query.on_trait_change(on_switch)
    page.on_trait_change(on_switch)

    for row in container.children:
        row.set_css({'width': '25%', 'align': 'left', 'background': '#e1e1e1'})
        for c in row.children:
            c.children[0].on_trait_change(on_switch, 'value')

    page_table(df)
    display(page)
