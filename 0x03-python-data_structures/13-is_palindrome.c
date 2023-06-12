#include "lists.h"
/**
 * list_len - Gives the length of a singly linked list
 * @head: Adress of the first element of the linked list
 *
 * Return: return the length of the linked list
 */
int list_len(listint_t **head)
{
	listint_t *buff = *head;
	int len = 1;

	if (buff == NULL)
		return (0);
	while (buff->next != NULL)
	{
		buff = buff->next;
		len++;
	}
	return (len);
}
/**
 * is_equal - Check if an element is equal to it's mirror
 * @head: Adress of the first element of the linked list
 * @index: The index of the value to check
 * @len: The length of the linked list
 *
 * Description: save the n value of the linked list element at position
 * index then check if it's equal to the element (len - (index + 1)).
 * Return: return 1 if the an element and it's mirror are equal
 * or 0 if not.
 */
int is_equal(listint_t **head, int index, int len)
{
	listint_t *buff = *head;
	int i, save;

	for (i = 0; i != index; i++)
		buff = buff->next;
	save = buff->n;
	while (i != (len - (index + 1)))
	{
		buff = buff->next;
		i++;
	}
	if (buff->n == save)
		return (1);
	return (0);
}
/**
 * is_palindrome - Check if a given linked list is a palindrome
 * @head: Adress of the first element of a linked list
 *
 * Return: return 1 if the linked list is a palindrome or 0 if not.
 */
int is_palindrome(listint_t **head)
{
	listint_t *buff = *head;
	int i, len = 0;

	len = list_len(&buff);
	if (len == 0)
		return (1);
	for (i = 0; i <= (len / 2) - 1; i++)
	{
		if (is_equal(&buff, i, len) == 0)
			return (0);
	}
	return (1);
}
