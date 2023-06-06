#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - Insert a new element in an ordered linked list
 * @head: The first element of the linked list
 * @number: The value of the n parameter of the new item
 *
 * Return: Return a pointer the newly created item or NUll
 * if an error occured.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *buff = *head;

	if (buff == NULL)
	{
		add_nodeint_end(head, number);
		return (buff);
	}
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	while ((buff->next != NULL) && (buff->next->n < new->n))
	{
		buff = buff->next;
	}
	if (buff->next != NULL)
	{
		if (buff == *head)
		{
			new->next = buff;
			*head = new;
		}
		else
		{
			new->next = buff->next;
			buff->next = new;
		}
	}
	else
		buff->next = new;
	return (new);
}
