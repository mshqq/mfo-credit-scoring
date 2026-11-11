import { Card, Flex, Typography, Table, Tag, type TableColumnsType } from 'antd';
import { applications, statuses, type ApplicationRow } from './TablesSection.data';

const columns: TableColumnsType<ApplicationRow> = [
  { title: '№ заявки', dataIndex: 'id' },
  { title: 'Клиент', dataIndex: 'client', sorter: (a, b) => a.client.localeCompare(b.client) },
  {
    title: 'Сумма',
    dataIndex: 'amount',
    render: (amount: number) => `${amount.toLocaleString('ru-RU')} ₽`,
    sorter: (a, b) => a.amount - b.amount,
  },
  { title: 'Срок', dataIndex: 'term', render: (term: number) => `${term} дней` },
  {
    title: 'Статус',
    dataIndex: 'status',
    render: (status: ApplicationRow['status']) => (
      <Tag color={statuses[status].color}>{statuses[status].label}</Tag>
    ),
    onFilter: (value, row) => row.status === value,
    filters: Object.entries(statuses).map(([value, { label }]) => ({ text: label, value })),
  },
];

export default function TablesSection() {
  return (
    <section id="tables">
      <Flex vertical align="baseline" style={{ marginBottom: '16px' }}>
        <Typography.Title level={2}>Таблицы</Typography.Title>
        <Typography.Text type="secondary">
          Список заявок с сортировкой, фильтром по статусу и переключением страниц.
        </Typography.Text>
      </Flex>
      <Card
        style={{ boxShadow: '0px 0px 50px 0px rgba(34, 60, 80, 0.15)' }}
        title="Заявки клиентов"
      >
        <Table<ApplicationRow>
          columns={columns}
          dataSource={applications}
          size="small"
          rowKey="id"
          pagination={{ pageSize: 4, showSizeChanger: false }}
        />
      </Card>
    </section>
  );
}
