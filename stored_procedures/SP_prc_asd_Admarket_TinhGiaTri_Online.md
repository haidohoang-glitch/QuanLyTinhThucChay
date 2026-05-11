# Stored Procedure: `prc_asd_Admarket_TinhGiaTri_Online`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-12-13 16:13:37.730000
- **Ngày sửa cuối**: 2021-06-29 14:39:23.650000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- ============================================
--exec [dbo].[prc_asd_Admarket_TinhGiaTri_Online] '2017-12-12'
CREATE PROCEDURE [dbo].[prc_asd_Admarket_TinhGiaTri_Online]
	-- Add the parameters for the stored procedure here
	@NgayThucHien datetime
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here

	delete [dbo].[ThucChayAdmarket_ADX_CPC_HopDong_online] where isnull(contract_number,'') <> ''
	delete [dbo].[ThucChayAdmarket_ViewPlus_HopDong_online] where isnull(contract_number,'') <> ''
	-- san pham 585
	insert into [dbo].[ThucChayAdmarket_ADX_CPC_HopDong_online]
	(
	   [user_id]
      ,[username]
      ,[isnoibo]
      ,[tt_click]
      ,[tt_view]
      ,[money]
      ,[promotion]
      ,[contract_number]
      ,[domain_name]
      ,[domain_tt_click]
      ,[domain_tt_view]
      ,[domain_money]
      ,[domain_promotion]
      ,[campaign_id]
      ,[DmSanPhamREF]
      ,[TenSanPham]
      ,[NgayThucHien]
      ,[createdBy]
      ,[createdAt]
      ,[DmViTriREF]
      ,[TenViTri]
      ,[contract_number_change]
      ,[data_type]
      ,[confirm_money]
      ,[confirm_tt_click]
      ,[confirm_tt_view]
      ,[giatrihopdong]
      ,[trangthai]
      ,[confirm_date]
      ,[confirm_status]
	)

	SELECT A.*,
	'',
	2,
	'',
	'',
	'',
	0,
	0,
	null,
	null
	FROM
	(
	SELECT 
	   [user_id]
      ,[username]
      ,'' is_NoiBo
      ,SUM(convert(money,[tt_click])) [tt_click]
      ,SUM(convert(money,[tt_view])) [tt_view]
      ,SUM(convert(money,[money])) [money]
      ,SUM(convert(money,[promotion])) [promotion]
      ,[contract_number]
      ,[domain_name]
      ,SUM(convert(money,[domain_tt_click])) [domain_tt_click]
      ,SUM(convert(money,[domain_tt_view])) [domain_tt_view]
      ,LTRIM(RTRIM(STR(SUM(convert(money,[domain_tt_money])/1.1) - ISNULL(( SELECT   SUM(GiaTriThayDoi + ThanhTienSauTrietKhauThucChay)
                                                   FROM     ThucChayDaTinhAdmarket c
                                                   WHERE    SoHopDong = a.contract_number
                                                            AND c.DmSanPhamREF = 585
															AND c.TenWebsite = a.domain_name
															AND c.DmViTriREF = CONVERT(INT,a.DmViTriREF)
                                                 ),0)))) [domain_tt_money]
      ,SUM(convert(money,[domain_tt_promotion])) [domain_tt_promotion]
      ,'' c
      ,[DmSanPhamREF]
      ,[TenSanPham]
      ,@NgayThucHien ngaythuchien
     ,'asd'  created_By
      ,@NgayThucHien created_at
      ,[DmViTriREF]
      ,[TenViTri]
  FROM [dbo].[ThucChayAdmarket_ADX_CPC_HopDong] a  where isnull(contract_number,'') <> '' 
  AND [isnoibo] = 0 
  AND domain_tt_money > 0 
  AND a.DmSanPhamREF= '585'
  and (select SUM(convert(money,[domain_tt_money])) from [ThucChayAdmarket_ADX_CPC_HopDong] b where b.contract_number = a.contract_number AND b.DmSanPhamREF = '585')
  > (select SUM(GiaTriThayDoi+ThanhTienSauTrietKhauThucChay) from ThucChayDaTinhAdmarket c where SoHopDong = a.contract_number AND c.DmSanPhamREF = 585)
  group by 
	   [user_id]
      ,[username]
	  ,[contract_number]
      ,[domain_name]

      ,[DmSanPhamREF]
      ,[TenSanPham]
      ,[DmViTriREF]
      ,[TenViTri]
	) A WHERE CONVERT(MONEY, A.[domain_tt_money]) >0
	-- san pham 144
	insert into [dbo].[ThucChayAdmarket_ADX_CPC_HopDong_online]
	(
	   [user_id]
      ,[username]
      ,[isnoibo]
      ,[tt_click]
      ,[tt_view]
      ,[money]
      ,[promotion]
      ,[contract_number]
      ,[domain_name]
      ,[domain_tt_click]
      ,[domain_tt_view]
      ,[domain_money]
      ,[domain_promotion]
      ,[campaign_id]
      ,[DmSanPhamREF]
      ,[TenSanPham]
      ,[NgayThucHien]
      ,[createdBy]
      ,[createdAt]
      ,[DmViTriREF]
      ,[TenViTri]
      ,[contract_number_change]
      ,[data_type]
      ,[confirm_money]
      ,[confirm_tt_click]
      ,[confirm_tt_view]
      ,[giatrihopdong]
      ,[trangthai]
      ,[confirm_date]
      ,[confirm_status]
	)

	SELECT A.*,
	'',
	2,
	'',
	'',
	'',
	0,
	0,
	null,
	null
	FROM
	(
	SELECT 
	   [user_id]
      ,[username]
      ,'' [isnoibo]
      ,SUM(convert(money,[tt_click])) [tt_click]
      ,SUM(convert(money,[tt_view])) [tt_view]
      ,SUM(convert(money,[money])) [money]
      ,SUM(convert(money,[promotion])) [promotion]
      ,[contract_number]
      ,[domain_name]
      ,SUM(convert(money,[domain_tt_click])) [domain_tt_click]
      ,SUM(convert(money,[domain_tt_view])) [domain_tt_view]
      , LTRIM(RTRIM(STR(SUM(convert(money,[domain_tt_money])/1.1)
	  -ISNULL(( SELECT   SUM(GiaTriThayDoi + ThanhTienSauTrietKhauThucChay)
                                                   FROM     ThucChayDaTinhAdmarket c
                                                   WHERE    SoHopDong = a.contract_number
                                                            AND c.DmSanPhamREF = 144
															AND c.TenWebsite = a.domain_name
															AND c.DmViTriREF = CONVERT(INT,a.DmViTriREF)
                                                 ),0)))) [domain_tt_money]
      ,SUM(convert(money,[domain_tt_promotion])) [domain_tt_promotion]
      ,'' ca
      ,[DmSanPhamREF]
      ,[TenSanPham]
      ,@NgayThucHien ngaythuchien
       ,'asd'  created_By
      ,@NgayThucHien created_at
      ,[DmViTriREF]
      ,[TenViTri]
  FROM [dbo].[ThucChayAdmarket_ADX_CPC_HopDong] a  where isnull(contract_number,'') <> '' 
  AND [isnoibo] = 0 
  AND domain_tt_money > 0 
  AND a.DmSanPhamREF= '144'
  and (select SUM(convert(money,[domain_tt_money])) from [ThucChayAdmarket_ADX_CPC_HopDong] b where b.contract_number = a.contract_number AND b.DmSanPhamREF = '144')
  > (select SUM(GiaTriThayDoi+ThanhTienSauTrietKhauThucChay) from ThucChayDaTinhAdmarket c where SoHopDong = a.contract_number AND c.DmSanPhamREF = 144)
  group by 
	   [user_id]
      ,[username]
	  ,[contract_number]
      ,[domain_name]
      ,[DmSanPhamREF]
      ,[TenSanPham]
      ,[DmViTriREF]
      ,[TenViTri]
	)  A WHERE   CONVERT(MONEY, A.[domain_tt_money]) >0
	--628
	insert into [dbo].[ThucChayAdmarket_ViewPlus_HopDong_online]
	(
	   [user_id]
      ,[username]
      ,[isnoibo]
      ,[tt_click]
      ,[tt_view]
      ,[money]
      ,[promotion]
      ,[contract_number]
      ,[domain_name]
      ,[domain_tt_click]
      ,[domain_tt_view]
      ,[domain_money]
      ,[domain_promotion]
      ,[campaign_id]
      ,[DmSanPhamREF]
      ,[TenSanPham]
      ,[NgayThucHien]
      ,[createdBy]
      ,[createdAt]
      ,[contract_number_change]
      ,[data_type]
      ,[confirm_money]
      ,[confirm_tt_click]
      ,[confirm_tt_view]
      ,[giatrihopdong]
      ,[trangthai]
      ,[confirm_date]
      ,[confirm_status]
	)

	SELECT A.*,
	'',
	2,
	'',
	'',
	'',
	0,
	0,
	null,
	null
	FROM
	(
	SELECT 
	   [user_id]
      ,[username]
      ,'' [isnoibo]
      ,SUM(convert(money,[tt_click])) [tt_click]
      ,SUM(convert(money,[tt_view])) [tt_view]
      ,SUM(convert(money,[money])) [money]
      ,SUM(convert(money,[promotion])) [promotion]
      ,[contract_number]
      ,[domain_name]
      ,SUM(convert(money,[domain_tt_click])) [domain_tt_click]
      ,SUM(convert(money,[domain_tt_view])) [domain_tt_view]
      ,LTRIM(RTRIM(STR(SUM(convert(money,[domain_money])/1.1) - ISNULL(( SELECT   SUM(GiaTriThayDoi + ThanhTienSauTrietKhauThucChay)
                                                   FROM     ThucChayDaTinhAdmarket c
                                                   WHERE    SoHopDong = a.contract_number
                                                            AND c.DmSanPhamREF = 628
															AND c.TenWebsite = a.domain_name
															
                                                 ),0)))) [domain_tt_money]
      ,SUM(convert(money,[domain_promotion])) [domain_tt_promotion]
      ,'' ca
      ,[DmSanPhamREF]
      ,[TenSanPham]
      ,@NgayThucHien ngaythuchien
     ,'asd'  created_By
      ,@NgayThucHien created_at
  FROM [dbo].[ThucChayAdmarket_ViewPlus_HopDong] a  where isnull(contract_number,'') <> '' and [isnoibo] = 0 AND domain_money >0
  AND a.DmSanPhamREF = '628'
  AND (select SUM(convert(money,[domain_money])) from [ThucChayAdmarket_ViewPlus_HopDong] b where b.contract_number = a.contract_number AND b.DmSanPhamREF = '628')
  > (select SUM(GiaTriThayDoi+ThanhTienSauTrietKhauThucChay) from ThucChayDaTinhAdmarket c where c.SoHopDong = a.contract_number AND c.DmSanPhamREF = 628)
  group by 
	   [user_id]
      ,[username]
	  ,[contract_number]
      ,[domain_name]
      ,[DmSanPhamREF]
      ,[TenSanPham]
	) A  WHERE   CONVERT(MONEY, A.[domain_tt_money]) >0

END

```
