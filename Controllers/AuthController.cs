using EmployeeHelper.UseCases.Login;
using EmployeeHelper.UseCases.Logout;
using EmployeeHelper.UseCases.Registration;
using EmployeeHelper.ViewModels;
using MediatR;
using Microsoft.AspNetCore.Mvc;
using System.ComponentModel.DataAnnotations;

namespace EmployeeHelper.Controllers;

[Route("authorization")]
public class AuthController : Controller
{
	private readonly IMediator mediator;

	public AuthController(IMediator mediator)
	{
		this.mediator = mediator;
	}

	[HttpPost("registration")]
	public async Task<IActionResult> Registration(RegistrationCommand command)
	{
		try
		{
			await mediator.Send(command);
		}
		catch (ValidationException ex)
		{
			ModelState.AddModelError(string.Empty, ex.Message);

			var viewModel = new RegistrationViewModel
			{
				FirstName = command.FirstName, 
				LastName = command.FirstName, 
				Surname = command.Surname, 
				Email = command.Email,
				PhoneNumber = command.PhoneNumber,
				Password = command.Password,
			};

			return View(viewModel);
		}

		return RedirectToAction(nameof(Login));
	}

	[HttpGet("registration")]
	public IActionResult Registration()
	{
		return View(new RegistrationViewModel());
	}

	[HttpPost("login")]
	public async Task<IActionResult> Login(LoginCommand command)
	{
		try
		{
			await mediator.Send(command);
		}
		catch (ValidationException ex)
		{
			ModelState.AddModelError(string.Empty, ex.Message);

			var viewModel = new AuthorizationViewModel
			{
				Email = command.Email,
				Password = command.Password,
			};

			return View(viewModel);
		}
		return RedirectToAction("");
	}

	[HttpGet("login")]
	public IActionResult Login()
	{
		return View(new AuthorizationViewModel());
	}


	[HttpPost("logout")]
	public async Task<IActionResult> Logout(LogoutCommand command)
	{
		await mediator.Send(command);

		return Ok();
	}
}