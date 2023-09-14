#include "lists.h"

/**
 * is_palindrome - Checks if the singly linked list is
 * palindrome
 * @head: A double pointer to the head of the list
 *
 * Return: 1 if list is a palindrome, 0 otherwise.
 */

int is_palindrome(listint_t **head)
{
	int arr[10000];
	int i, n = 0;
	listint_t *traverse;

	if (head == NULL)
		return (0);

	/* Copy the numbers from Linked List to arr */
	traverse = *head;
	while (traverse)
	{
		arr[n++] = traverse->n;
		traverse = traverse->next;
	}

	/* Check if the given arr is a palindrome */
	for (i = 0; i < n / 2; i++)
	{
		if (arr[i] != arr[n - i - 1])
			return (0);
	}
	return (1);
}
