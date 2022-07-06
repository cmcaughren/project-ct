import sqlalchemy as sa


class BasicMetrics():
    created_timestamp = sa.Column(sa.DateTime)
    last_updated_timestamp = sa.Column(sa.DateTime)


# TODO: implement list of column to class columns conversion method
class AutoColumn():

    @classmethod
    def auto_column(columns):
        raise NotImplementedError
