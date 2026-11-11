export type ApplicationRow = {
  id: number;
  client: string;
  amount: number;
  term: number;
  status: keyof typeof statuses;
};

export const applications: ApplicationRow[] = [
  {
    id: 10482,
    client: 'Иванов Иван Иванович',
    amount: 50000,
    term: 30,
    status: 'pending',
  },
  {
    id: 10481,
    client: 'Петрова Анна Сергеевна',
    amount: 30000,
    term: 14,
    status: 'approved',
  },
  { id: 10480, client: 'Смирнов Алексей Олегович', amount: 10000, term: 7, status: 'rejected' },
  { id: 10479, client: 'Соколова Мария Андреевна', amount: 25000, term: 30, status: 'draft' },
  { id: 10478, client: 'Кузнецов Дмитрий Павлович', amount: 15000, term: 14, status: 'approved' },
  { id: 10477, client: 'Волкова Елена Игоревна', amount: 40000, term: 30, status: 'pending' },
];

export const statuses = {
  pending: { label: 'На проверке', color: '#f5a216' },
  approved: { label: 'Одобрено', color: '#72C55F' },
  rejected: { label: 'Отказано', color: '#EF4444' },
  draft: { label: 'Черновик', color: '#3B82F6' },
};
