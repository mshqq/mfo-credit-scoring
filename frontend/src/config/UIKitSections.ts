import {
  IdCard,
  LayoutPanelTop,
  SquareCheckBig,
  Palette,
  SquarePower,
  TableCellsMerge,
  TypeOutline,
  BellRing,
  Tags,
  PiggyBank,
  ClipboardPenLine,
} from 'lucide-react';

export const uiKitSections = [
  { id: 'overview', label: 'Обзор', icon: PiggyBank },
  { id: 'colors', label: 'Цвета', icon: Palette },
  { id: 'typography', label: 'Типографика', icon: TypeOutline },
  { id: 'buttons', label: 'Кнопки', icon: SquarePower },
  { id: 'inputs', label: 'Поля ввода', icon: ClipboardPenLine },
  { id: 'selects', label: 'Выборы', icon: SquareCheckBig },
  { id: 'tables', label: 'Таблицы', icon: TableCellsMerge },
  { id: 'cards', label: 'Карточки', icon: IdCard },
  { id: 'modals', label: 'Модальные окна', icon: LayoutPanelTop },
  { id: 'notifications', label: 'Уведомления', icon: BellRing },
  { id: 'tags', label: 'Теги и статусы', icon: Tags },
];
