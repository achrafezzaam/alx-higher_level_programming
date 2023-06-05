#include "lists.h"
/**
 * check_cycle - Check if there is a loop in a linked list
 * @list: pointer to the list to check
 *
 * Return: return 0 if no loop was found and 1 if a loop was found
 */
int check_cycle(listint_t *list)
{
	listint_t *elem1, *elem2;

	if (list == NULL || list->next == NULL)
		return (0);

	elem1 = list->next;
	elem2 = list->next->next;
	while (elem1 != NULL && elem2 != NULL && elem2->next != NULL)
	{
		if (elem1 == elem2)
			return (1);
		elem1 = elem1->next;
		elem2 = elem2->next;
	}
	return (0);
}
