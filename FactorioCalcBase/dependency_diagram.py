import plotly.graph_objects as go


class DependencyDiagram:
    def __init__(self, conf, diagram_data: dict):
        self.diagram_data = diagram_data
        self.fig = go.Figure(
            data=[go.Sankey(
                node=dict(
                    line=dict(
                        color='black',
                        width=0
                    ),
                    pad=100,
                    thickness=50,
                    label=self.diagram_data.get('node'),
                    customdata=self.diagram_data.get('node_custom_data'),
                    hovertemplate='%{customdata}'
                ),
                link=dict(
                    source=self.diagram_data.get('source'),
                    target=self.diagram_data.get('target'),
                    value=self.diagram_data.get('value'),
                    label=self.diagram_data.get('label'),
                    customdata=self.diagram_data.get('link_custom_data'),
                    hovertemplate='%{customdata}'

                ),
            )]
        )
        layout = dict(
            title_text=conf.recipe_name,
            font_size=15,
        )
        self.fig.update_layout(layout)

    def get_html(self):
        return self.fig.to_html()
