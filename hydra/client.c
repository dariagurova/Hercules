/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   client.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dgurova <dariagurova91@gmail.com>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/03/01 22:18:39 by dgurova           #+#    #+#             */
/*   Updated: 2018/03/01 22:18:41 by dgurova          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>

# define BUFF_SIZE (1024)

int main()
{
	int					sockfd;
	int					port;
	struct sockaddr_in	server_addr;
	char				buf[BUFF_SIZE + 1];

	sockfd = socket(AF_INET, SOCK_STREAM, 0);
	printf("What is the port number to connect to?:\n");
	scanf("%d", &port);
	server_addr.sin_family = AF_INET;
	server_addr.sin_addr.s_addr = INADDR_ANY; 
	server_addr.sin_port = htons(port);
	if(connect(sockfd, (struct sockaddr*)&server_addr, sizeof(server_addr)) != 0)
	{
		printf("Connection to server failed!\n");
		exit(1);
	}
	printf("Connected to Server on port %d\n", port);
	while(1) 
	{
		printf("Message to server: ");
		bzero(buf, BUFF_SIZE);
		scanf("%s", buf);
		if (strncmp(buf, "quit", 5) == 0)
		{
			printf("Exit\n");
			exit(1);
		}

		write(sockfd, buf, strlen(buf));
		bzero(buf, BUFF_SIZE);
		read(sockfd, buf, BUFF_SIZE);
		printf("Message from server: %s\n", buf);
	}
	close(sockfd);
	return (0);
}