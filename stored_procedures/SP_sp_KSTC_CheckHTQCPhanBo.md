# Stored Procedure: `sp_KSTC_CheckHTQCPhanBo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-05-15 11:59:13.463000
- **Ngày sửa cuối**: 2020-09-22 15:27:44.523000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_KSTC_CheckHTQCPhanBo]
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	-- 1.Treo chi phí
	select N'Treo chi phí' [Nhom],b.product_formality_id htqc_hd, a.product_formality_id htqc_treo,a.LastmodifiedAt ,a.* 
	from [192.168.23.150].thuctreo.dbo.thuctreo_chiphi a left join [192.168.23.150].contract.dbo.contract_details b
on a.contract_detail_id = b.id 
where a.product_formality_id <> b.product_formality_id
and a.DeletedStatus = 0
and b.Deleted_Status =0
and a.TotalMoney <> 0
and a.LastmodifiedAt >='2020-01-01'
order by a.LastmodifiedAt  desc

	-- 2.Treo branding
	select N'Treo branding' [Nhom],b.product_formality_id htqc_hd,a.product_formality_id htqc_treo,a.Last_Modified_At,a.* 
	from [192.168.23.150].thuctreo.dbo.thuctreo a left join [192.168.23.150].contract.dbo.contract_details b
on a.contract_detail_id = b.id 
where a.product_formality_id <> b.product_formality_id
and a.Deleted_Status = 0
and b.Deleted_Status =0
and a.Last_Modified_At >='2020-01-01'
and a.Id not in (124885) --id treo của chi phí
order by a.Last_Modified_At desc

	-- 3.Treo pr
	--select top 1 * from [asd14].contract.dbo.contract_details
	select N'Treo pr' [Nhom],a.contract_number ,a.id idtreo,b.product_formality_id htqc_hd,a.product_formality_id htqc_treo,b.product_id sp_hd,a.product_id sp_treo,
	a.contract_detail_id, a.contract_id,b.PRICE PRICE_hd,
	b.Last_Modified_At hd,a.Last_Modified_At treo
	from [192.168.23.150].thuctreo.dbo.thuctreo_pr a left join [192.168.23.150].contract.dbo.contract_details b
on a.contract_detail_id = b.id 
where a.product_formality_id <> b.product_formality_id
and a.Deleted_Status = 0
and b.Deleted_Status =0
and a.Last_Modified_At >='2020-01-01'
order by a.Last_Modified_At desc
END

```
