#include "lists.h"

/**
 * check_cycle - To check if singly-linked list contains a cycle
 * @list: Singly-linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *link1, *link2;

	if (list == NULL || list->next == NULL)
		return (0);

	link1 = list->next;
	link2 = list->next->next;

	while (link1 && link2 && link2->next)
	{
		if (link1 == link2)
			return (1);

		link1 = link1->next;
		link2 = link2->next->next;
	}

	return (0);
}
