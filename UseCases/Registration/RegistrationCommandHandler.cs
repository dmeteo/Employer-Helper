using EmployeeHelper.Domain;
using MediatR;
using Microsoft.AspNetCore.Identity;
using System.ComponentModel.DataAnnotations;

namespace EmployeeHelper.UseCases.Registration;

public class RegistrationCommandHandler : IRequestHandler<RegistrationCommand, Unit>
{
	private readonly UserManager<User> userManager;

	public RegistrationCommandHandler(UserManager<User> userManager)
	{
		this.userManager = userManager;
	}

	public async Task<Unit> Handle(RegistrationCommand request, CancellationToken cancellationToken)
	{
		if (userManager.Users.Any(u => u.Email == request.Email))
		{
			throw new ValidationException("Such user already exists.");
		}

		var user = new User
		{
			UserName = request.FirstName + request.LastName,	
			FirstName = request.FirstName,
			LastName = request.LastName,
			Surname = request.Surname,
			Email = request.Email,
			PhoneNumber = request.PhoneNumber,
		};

		var result = await userManager.CreateAsync(user, request.Password);

		if (!result.Succeeded)
		{
			var errorString = string.Join(Environment.NewLine, result.Errors);
			throw new ValidationException(errorString);
		}

		return Unit.Value;
	}
}