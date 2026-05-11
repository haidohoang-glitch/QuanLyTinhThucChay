# Stored Procedure: `Gen_InsertOrUpdate_AppKetQuaVanHanh_CreatorContent`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-25 16:28:47.800000
- **Ngày sửa cuối**: 2021-10-29 09:32:47.050000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
/*
EXEC [dbo].[Gen_InsertOrUpdate_AppKetQuaVanHanh_CreatorContent]

*/
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_AppKetQuaVanHanh_CreatorContent] 	
As 	
BEGIN
	DECLARE @NgayThucHien DATETIME
	DECLARE @SQL NVARCHAR(MAX),@server_id nvarchar(100) = '', @database nvarchar(100) = '', @daunhay nvarchar(10) = '''',
	@server_id_contract nvarchar(100) = '', @database_contract nvarchar(100) = ''
	SET @NgayThucHien = 
		ISNULL((
			SELECT  MAX(kq.LastModificationTime)
			FROM   dbo.AppKetQuaVanHanh_CreatorContent kq
		),'2017-01-01')

	SET @server_id =
	ISNULL((SELECT TOP (1) (SERVER_ID) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'CREATORCONTENT' ORDER BY id),'')

	SET @database= 
	ISNULL((SELECT TOP (1) (DATA_NAME) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'CREATORCONTENT' ORDER BY id),'')

	SET @server_id_contract =
	ISNULL((SELECT TOP (1) (SERVER_ID) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'CONTRACT' ORDER BY id),'')

	SET @database_contract= 
	ISNULL((SELECT TOP (1) (DATA_NAME) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'CONTRACT' ORDER BY id),'')

	SET @NgayThucHien = DATEADD(HOUR,-8,@NgayThucHien)

	PRINT @NgayThucHien

	CREATE TABLE #AppKetQuaVanHanh_CreatorContent(
		[AppKetQuaVanHanh_CreatorContent_id] [int] NOT NULL,
		[HopDongBanRef] [int] NULL,
		[PhanBoRef] [int] NULL,
		[PbSoLuong] [int] NULL,
		[pbDonGia] [decimal](18, 2) NULL,
		[PbChietKhau] [decimal](18, 2) NULL,
		[PbThanhTien] [decimal](18, 2) NULL,
		[NgayThucHien] [datetime] NULL,
		[Link] [nvarchar](2500) NULL,
		[TcDonGia] FLOAT NULL,
		[TcSoLuong] [int] NULL,
		[TcDonViTinhREF] [int] NULL,
		[DonViTinh] nvarchar(100) NULL,
		[TcThanhTien] [decimal](18, 2) NULL,
		[AppPageKolRef] [int] NULL,
		[AppHangMucRef] [int] NULL,
		[AppHopDongKolRef] [int] NULL,
		[DonGia] [decimal](18, 2) NULL,
		[ChietKhau] [decimal](18, 2) NULL,
		[ThanhTien] [decimal](18, 2) NULL,
		[VAT] [decimal](8, 2) NULL,
		[TienThanhToan] [decimal](18, 2) NULL,
		[LaiLo] [decimal](18, 2) NULL,
		[TrangThai] [tinyint] NULL,
		[NguoiDuyet] [int] NULL,
		[NguoiDuyetTen] [nvarchar](250) NULL,
		[NgayDuyet] [datetime] NULL,
		[NguoiDuyetTT] [int] NULL,
		[NguoiDuyetTTTen] [nvarchar](250) NULL,
		[NgayDuyetTT] [datetime] NULL,
		[NguoiTuChoi] [int] NULL,
		[NguoiTuChoiTen] [nvarchar](250) NULL,
		[NgayTuChoi] [datetime] NULL,
		[LyDoTuChoi] [nvarchar](500) NULL,
		[NguoiTuChoiTT] [int] NULL,
		[NguoiTuChoiTTTen] [nvarchar](250) NULL,
		[NgayTuChoiTT] [datetime] NULL,
		[LyDoTuChoiTT] [nvarchar](500) NULL,
		[CreationTime] [datetime2](7) NULL,
		[CreatorUserId] [bigint] NULL,
		[CreatedBy] [nvarchar](100) NULL,
		[LastModificationTime] [datetime2](7) NULL,
		[LastModifierUserId] [bigint] NULL,
		[LastModifiedBy] [nvarchar](100) NULL,
		[DeletionTime] [datetime2](7) NULL,
		[DeleterUserId] [bigint] NULL,
		[IsDeleted] [bit] NULL,
		[NgayGuiDuyet] [datetime] NULL,
		[NguoiGuiDuyet] [int] NULL,
		[NguoiGuiDuyetTen] [nvarchar](250) NULL,
		[NgayGuiDuyetTT] [datetime] NULL,
		[NguoiGuiDuyetTT] [int] NULL,
		[NguoiGuiDuyetTTTen] [nvarchar](250) NULL,
		[Record_Status] smallint)

	SET @SQL = 
	'INSERT INTO #AppKetQuaVanHanh_CreatorContent '

	SET @SQL +=
	'SELECT kq.[Id] as [AppKetQuaVanHanh_CreatorContent_id]
      ,kq.[HopDongBanRef]
      ,kq.[PhanBoRef]
      ,kq.[PbSoLuong]
      ,kq.[pbDonGia]
      ,kq.[PbChietKhau]
      ,kq.[PbThanhTien]
      ,kq.[NgayThucHien]
      ,kq.[Link]
	  ,kq.[TcDonGia]
      ,kq.[TcSoLuong]
	  ,isnull(kq.[TcDonViTinh],0) as TcDonViTinhRef
	  ,ISNull((SELECT top (1) u.[name] FROM ' + @server_id_contract + '.' + @database_contract + '.dbo.UNITS u where u.id = kq.[TcDonViTinh] ORDER BY u.id),'''') AS DonViTinh
      ,kq.[TcThanhTien]
      ,kq.[AppPageKolRef]
      ,kq.[AppHangMucRef]
      ,kq.[AppHopDongKolRef]
      ,kq.[DonGia]
      ,kq.[ChietKhau]
      ,kq.[ThanhTien]
      ,kq.[VAT]
      ,kq.[TienThanhToan]
      ,kq.[LaiLo]
      ,kq.[TrangThai]
      ,kq.[NguoiDuyet]
      ,kq.[NguoiDuyetTen]
      ,kq.[NgayDuyet]
      ,kq.[NguoiDuyetTT]
      ,kq.[NguoiDuyetTTTen]
      ,kq.[NgayDuyetTT]
      ,kq.[NguoiTuChoi]
      ,kq.[NguoiTuChoiTen]
      ,kq.[NgayTuChoi]
      ,kq.[LyDoTuChoi]
      ,kq.[NguoiTuChoiTT]
      ,kq.[NguoiTuChoiTTTen]
      ,kq.[NgayTuChoiTT]
      ,kq.[LyDoTuChoiTT]
      ,kq.[CreationTime]
      ,kq.[CreatorUserId]
	  ,(SELECT TOP (1) U.UserName FROM  ' + @server_id + '.' + @database + '.[dbo].AbpUsers U WHERE U.ID = kq.[CreatorUserId] ORDER BY U.Id) AS CreatedBy
      ,kq.[LastModificationTime]
      ,kq.[LastModifierUserId]
	  ,(SELECT TOP (1) U.UserName FROM ' + @server_id + '.' + @database + '.[dbo].AbpUsers U WHERE U.ID = kq.[LastModifierUserId] ORDER BY U.Id) AS LastModifiedBy
      ,kq.[DeletionTime]
      ,kq.[DeleterUserId]
      ,kq.[IsDeleted]
      ,kq.[NgayGuiDuyet]
      ,kq.[NguoiGuiDuyet]
      ,kq.[NguoiGuiDuyetTen]
      ,kq.[NgayGuiDuyetTT]
      ,kq.[NguoiGuiDuyetTT]
      ,kq.[NguoiGuiDuyetTTTen]
	  ,0 [Record_Status]
	  FROM ' + @server_id + '.' + @database + '.[dbo].[AppKetQuaVanHanh] kq
	  WHERE kq.LastModificationTime >= ' + @daunhay + convert(nvarchar(23),@ngaythuchien,121)+ @daunhay+' '
				
	--PRINT @SQL
	EXEC(@SQL)

	UPDATE t 
	SET   t.[Record_Status] = 1
	FROM  #AppKetQuaVanHanh_CreatorContent t INNER JOIN dbo.AppKetQuaVanHanh_CreatorContent dc
	ON t.AppKetQuaVanHanh_CreatorContent_id = dc.AppKetQuaVanHanh_CreatorContent_id

-- Update nhung row da ton ton                                      
	UPDATE dc
	SET dc.[HopDongBanRef] = t.HopDongBanRef
		,dc.[PhanBoRef] = t.PhanBoRef
		,dc.[PbSoLuong] = t.PbSoLuong
		,dc.[pbDonGia] = t.pbDonGia
		,dc.[PbChietKhau] = t.PbChietKhau
		,dc.[PbThanhTien] = t.PbThanhTien
		,dc.[NgayThucHien] = t.NgayThucHien
		,dc.[Link] = t.Link
		,dc.[TcDonGia] = t.TcDonGia
		,dc.[TcSoLuong] = t.TcSoLuong
		,dc.[TcDonViTinhREF] = t.TcDonViTinhREF
		,dc.[DonViTinh] = t.DonViTinh
		,dc.[TcThanhTien] = t.TcThanhTien
		,dc.[AppPageKolRef] = t.AppPageKolRef
		,dc.[AppHangMucRef] = t.AppHangMucRef
		,dc.[AppHopDongKolRef] = t.AppHopDongKolRef
		,dc.[DonGia] = t.DonGia
		,dc.[ChietKhau] = t.ChietKhau
		,dc.[ThanhTien] = t.ThanhTien
		,dc.[VAT] = t.VAT
		,dc.[TienThanhToan] = t.TienThanhToan
		,dc.[LaiLo] = t.LaiLo
		,dc.[TrangThai] = t.TrangThai
		,dc.[NguoiDuyet] = t.NguoiDuyet
		,dc.[NguoiDuyetTen] = t.NguoiDuyetTen
		,dc.[NgayDuyet] = t.NgayDuyet
		,dc.[NguoiDuyetTT] = t.NguoiDuyetTT
		,dc.[NguoiDuyetTTTen] = t.NguoiDuyetTTTen
		,dc.[NgayDuyetTT] = t.NgayDuyetTT
		,dc.[NguoiTuChoi] = t.NguoiTuChoi
		,dc.[NguoiTuChoiTen] = t.NguoiTuChoiTen
		,dc.[NgayTuChoi] = t.NgayTuChoi
		,dc.[LyDoTuChoi] = t.LyDoTuChoi
		,dc.[NguoiTuChoiTT] = t.NguoiTuChoiTT
		,dc.[NguoiTuChoiTTTen] = t.NguoiTuChoiTTTen
		,dc.[NgayTuChoiTT] = t.NgayTuChoiTT
		,dc.[LyDoTuChoiTT] = t.LyDoTuChoiTT
		,dc.[CreationTime] = t.CreationTime
		,dc.[CreatorUserId] = t.CreatorUserId
		,dc.[CreatedBy] = t.CreatedBy
		,dc.[LastModificationTime] = t.LastModificationTime
		,dc.[LastModifierUserId] = t.LastModifierUserId
		,dc.[LastModifiedBy] = t.LastModifiedBy
		,dc.[DeletionTime] = t.DeletionTime
		,dc.[DeleterUserId] = t.DeleterUserId
		,dc.[IsDeleted] = t.IsDeleted
		,dc.[NgayGuiDuyet] = t.NgayGuiDuyet
		,dc.[NguoiGuiDuyet] = t.NguoiGuiDuyet
		,dc.[NguoiGuiDuyetTen] = t.NguoiGuiDuyetTen
		,dc.[NgayGuiDuyetTT] = t.NgayGuiDuyetTT
		,dc.[NguoiGuiDuyetTT] = t.NguoiGuiDuyetTT
		,dc.[NguoiGuiDuyetTTTen] = t.NguoiGuiDuyetTTTen
	FROM dbo.AppKetQuaVanHanh_CreatorContent dc INNER JOIN  #AppKetQuaVanHanh_CreatorContent t 
		ON t.AppKetQuaVanHanh_CreatorContent_id = dc.AppKetQuaVanHanh_CreatorContent_id
	WHERE t.Record_Status = 1


	-- Insert Row chua ton tai
	INSERT INTO [dbo].[AppKetQuaVanHanh_CreatorContent]
           ([AppKetQuaVanHanh_CreatorContent_id]
           ,[HopDongBanRef]
           ,[PhanBoRef]
           ,[PbSoLuong]
           ,[pbDonGia]
           ,[PbChietKhau]
           ,[PbThanhTien]
           ,[NgayThucHien]
           ,[Link]
		   ,[TcDonGia]
           ,[TcSoLuong]
		   ,[TcDonViTinhREF]
		   ,DonViTinh
           ,[TcThanhTien]
           ,[AppPageKolRef]
           ,[AppHangMucRef]
           ,[AppHopDongKolRef]
           ,[DonGia]
           ,[ChietKhau]
           ,[ThanhTien]
           ,[VAT]
           ,[TienThanhToan]
           ,[LaiLo]
           ,[TrangThai]
           ,[NguoiDuyet]
           ,[NguoiDuyetTen]
           ,[NgayDuyet]
           ,[NguoiDuyetTT]
           ,[NguoiDuyetTTTen]
           ,[NgayDuyetTT]
           ,[NguoiTuChoi]
           ,[NguoiTuChoiTen]
           ,[NgayTuChoi]
           ,[LyDoTuChoi]
           ,[NguoiTuChoiTT]
           ,[NguoiTuChoiTTTen]
           ,[NgayTuChoiTT]
           ,[LyDoTuChoiTT]
           ,[CreationTime]
           ,[CreatorUserId]
           ,[CreatedBy]
           ,[LastModificationTime]
           ,[LastModifierUserId]
           ,[LastModifiedBy]
           ,[DeletionTime]
           ,[DeleterUserId]
           ,[IsDeleted]
           ,[NgayGuiDuyet]
           ,[NguoiGuiDuyet]
           ,[NguoiGuiDuyetTen]
           ,[NgayGuiDuyetTT]
           ,[NguoiGuiDuyetTT]
           ,[NguoiGuiDuyetTTTen]
		   ,[RecordStatus]
		   ,[ThanhTienSauChietKhauThucChay]
		   ,[NgayGhiNhanThucChay]) --trang thai ban ghi cho viec tinh thuc chay hay chua: 0 chua tinh, 1 da tinh
    

	SELECT [AppKetQuaVanHanh_CreatorContent_id]
		  ,[HopDongBanRef]
		  ,[PhanBoRef]
		  ,[PbSoLuong]
		  ,[pbDonGia]
		  ,[PbChietKhau]
		  ,[PbThanhTien]
		  ,[NgayThucHien]
		  ,[Link]
		  ,[TcDonGia]
		  ,[TcSoLuong]
		  ,[TcDonViTinhREF]
		  ,DonViTinh
		  ,[TcThanhTien]
		  ,[AppPageKolRef]
		  ,[AppHangMucRef]
		  ,[AppHopDongKolRef]
		  ,[DonGia]
		  ,[ChietKhau]
		  ,[ThanhTien]
		  ,[VAT]
		  ,[TienThanhToan]
		  ,[LaiLo]
		  ,[TrangThai]
		  ,[NguoiDuyet]
		  ,[NguoiDuyetTen]
		  ,[NgayDuyet]
		  ,[NguoiDuyetTT]
		  ,[NguoiDuyetTTTen]
		  ,[NgayDuyetTT]
		  ,[NguoiTuChoi]
		  ,[NguoiTuChoiTen]
		  ,[NgayTuChoi]
		  ,[LyDoTuChoi]
		  ,[NguoiTuChoiTT]
		  ,[NguoiTuChoiTTTen]
		  ,[NgayTuChoiTT]
		  ,[LyDoTuChoiTT]
		  ,[CreationTime]
		  ,[CreatorUserId]
		  ,[CreatedBy]
		  ,[LastModificationTime]
		  ,[LastModifierUserId]
		  ,[LastModifiedBy]
		  ,[DeletionTime]
		  ,[DeleterUserId]
		  ,[IsDeleted]
		  ,[NgayGuiDuyet]
		  ,[NguoiGuiDuyet]
		  ,[NguoiGuiDuyetTen]
		  ,[NgayGuiDuyetTT]
		  ,[NguoiGuiDuyetTT]
		  ,[NguoiGuiDuyetTTTen]
		  ,0 AS RecordStatus --trang thai ban ghi da tinh thuc chay hay chua
		  ,0 AS ThanhTienSauChietKhauThucChay
		  ,'1900-01-01' AS NgayGhiNhanThucChay
	  FROM #AppKetQuaVanHanh_CreatorContent
	  WHERE Record_Status = 0 --trang thai ban ghi cho viec syn du lieu

	DROP TABLE #AppKetQuaVanHanh_CreatorContent
END

--select * from dbo.AppKetQuaVanHanh_CreatorContent
```
