using EmployeeHelper.Domain;
using EmployeeHelper.UseCases.Login;
using MediatR;
using Microsoft.AspNetCore.Identity;
using System.ComponentModel.DataAnnotations;

namespace EmployeeHelper.Web.UseCases.Login;

public class LoginCommandHandler : IRequestHandler<LoginCommand, Unit>
{
	private SignInManager<User> signInManager;
	private UserManager<User> userManager;

	public LoginCommandHandler(SignInManager<User> signInManager, UserManager<User> userManager)
	{
		this.userManager = userManager;
		this.signInManager = signInManager;
	}

	public async Task<Unit> Handle(LoginCommand request, CancellationToken cancellationToken)
	{
		var user = await userManager.FindByNameAsync(request.UserName);

		if (user == null)
		{
			throw new ValidationException("Such user does not exists");
		}

		request.ToString();

		var result = await signInManager.PasswordSignInAsync(user, request.Password, isPersistent: true, lockoutOnFailure: false);

		if (!result.Succeeded)
		{
			throw new ValidationException("Password or username is not correct.");
		}

		return Unit.Value;
	}
}